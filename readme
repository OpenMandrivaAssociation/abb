abb
===

`abb` builds RPMs locally with `rpmbuild` and submits builds to OpenMandriva's
Automated Build Farm (ABF). It also uploads and restores source files and
requests publication of ABF builds.

Requirements
------------

The `abb` RPM depends on bash, git-core, curl, wget and rpm-build. Local
builds also need the `BuildRequires` listed in the package spec. Install w3m
for `abb view` or lynx for the legacy `abb status` command.

Build locally
-------------

Clone the zlib packaging repository and build its binary RPMs.

    abb clone zlib branch=
    cd zlib
    abb build

`clone` fetches repositories from `OpenMandrivaAssociation` on GitHub. It
defaults to `branch=master` and `remote=origin`. An empty `branch=` keeps
the branch checked out by `git clone`.

`restore` controls automatic source downloads after `clone` and before
`build`. `restore=always` is the default, `restore=ask` prompts first, and
`restore=none` skips automatic downloads. Run `abb restore` to fetch missing
sources explicitly with any of these settings.

Run `build` in a checkout with one spec file. A one-letter suffix selects
the corresponding `rpmbuild -b<stage>` action.

    abb command      rpmbuild action
    build, buildb     -bb  Build binary RPMs (default)
    builda            -ba  Build binary and source RPMs
    builds            -bs  Build the source RPM
    buildp            -bp  Prepare sources (%prep)
    buildc            -bc  Build through %build
    buildi            -bi  Build through %install without packaging
    buildl            -bl  Check the %files list after a run through %install

Pass extra rpmbuild flags after the command. `abb buildi --short-circuit`
skips the earlier stages and uses an existing build tree. With the default
`buildlog=yes`, abb saves the output to a `.buildlog` file.

Submit a build to ABF
---------------------

You need an ABF account with permission to build the project. Get your API
token from https://abf.openmandriva.org/settings/private. For HTTP Basic
authentication over HTTPS, set `auth` to `TOKEN:` or `LOGIN:PASSWORD`.

Run this from the package checkout with `auth` unset in your config. It
prompts for the token and submits a test build with autopublish disabled.

    (
        read -r -s -p 'ABF API token: ' abf_token && printf '\n' &&
            auth="${abf_token}:" abb send arch="x86_64 znver1 aarch64" publish=false
    )

Keep ABF credentials scoped to ABF commands. `clone` and `view` also use
`auth` when they build GitHub URLs.

`send` takes one optional project name and otherwise infers it from the
checkout. Push your changes before submitting the Git branch or commit to
ABF. `send` prints a build-list ID for each accepted request.

OpenMandriva usually builds for `x86_64`, `znver1` and `aarch64`. By default,
abb tries a separate request for each of the five targets below, including
`i686` and `armv7hnl`. It skips architecture names ABF does not recognize.
Pass a quoted, space-separated `arch` value to choose the targets.

Built-in defaults for `send`

    arch="i686 x86_64 armv7hnl aarch64 znver1"
    platform=cooker
    publish=true

`platform` selects the ABF build platform. With `publish=true`, abb asks ABF
to publish successful builds automatically.

Other submission options

    branch=master      Git branch to build.
    commit=            Use a full commit hash instead of the branch.
    repos=             Repositories to include, for example main,contrib.
    reposave=          Destination in platform/repo form, for example
                       cooker/main if the project is linked to that repo.
                       If omitted, abb uses the project's repository for
                       the build platform.
    updatetype=security
                       Update type. Other values are bugfix, enhancement,
                       recommended and newpackage.
    withrequired=false
                       Set to true to request a rebuild of reverse dependencies.

Check builds at https://abf.openmandriva.org/build_lists.

Command reference
-----------------

    abb clone <project> ...
        Clone one or more package repositories.

    abb new <project>
        Initialize a local Git repository with an origin URL. If the spec
        skeleton is readable, create <project>.spec from it. Override the
        default skeleton at /usr/share/abb/spek.skel with `defaultspec`.

    abb build [<project> ...]
        Restore sources according to `restore` and run rpmbuild locally.
        With no project argument, build from the current directory.

    abb restore [<project> ...]
        Download missing files listed in .abf.yml from
        https://file-store.openmandriva.org and check their SHA-1 sums.
        With no project argument, use the current directory.

    abb store <file> ...
        Run from the package checkout. Upload source files to the OpenMandriva
        file store and record their names and SHA-1 sums in .abf.yml.

    abb send [<project>]
        Submit remote build requests to ABF.

    abb view [<project>|<build-list-id>]
        Open a package repository on GitHub or an ABF build-list page in w3m.

    abb status [<project>]
        Legacy command. Queries a GitHub project path that returns 404 for
        projects such as zlib. Use the ABF build lists page.

    abb publish <build-list-id> ...
    abb rejectpublish <build-list-id> ...
        Request publication or reject publication of the specified ABF builds.

    abb vars [<setting> ...]
        Print effective settings. For example, `abb vars arch platform publish`
        shows the targets, platform and publication setting `send` would use.

Configuration
-------------

abb reads Bash assignments from ~/.abbrc, or from .abbrc in the current
directory if ~/.abbrc is absent. Pass supported settings as `name=value`
arguments to override the configuration file for one invocation.

The ABF API defaults to `https://abf.openmandriva.org/api/v1`.
Set `owner` to the project owner in ABF (default `openmandriva`). The
`abfyml` setting selects the source manifest (default `.abf.yml`).
