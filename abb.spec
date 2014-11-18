name:		abb
version:	0.5
release:	5
summary:	command-line client for abf.rosalinux.ru

group:		System/Configuration/Packaging
license:	GPLv3+
url:		git://github.com/sash-kan/%{name}.git
buildarch:	noarch
source0:	%{name}
source1:	%{name}rc
source2:	readme
source3:	gpl-3.0.txt
source4:	spek.skel
source5:	abb.json.sh
source6:	license.apache2
source7:	license.mit
source8:	abb.bash_completion

requires:	bash
requires:	git-core
# w3m in contrib repo
#suggests:	w3m
requires:	curl
suggests:	lynx
requires:	wget
requires:	rpm-build

buildarch:	noarch

%description
abb is command-line client for <http://abf.rosalinux.ru>

%prep
%setup -qcT
cp %{SOURCE1} .
cp %{SOURCE2} .

%install
install -d %{buildroot}%{_bindir}
install %{SOURCE0} %{buildroot}%{_bindir}/
install -d %{buildroot}%{_datadir}/%{name}
install %{SOURCE4} %{buildroot}%{_datadir}/%{name}/
install %{SOURCE5} %{buildroot}%{_bindir}/
install -d %{buildroot}%{_datadir}/bash_completion
install %{SOURCE8} %{buildroot}%{_datadir}/bash_completion/abb
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
ln -s %{_datadir}/bash_completion/abb %{buildroot}%{_sysconfdir}/bash_completion.d/abb

%files
%doc abbrc readme
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/bash_completion
%{_sysconfdir}/bash_completion.d
