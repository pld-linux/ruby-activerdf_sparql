Summary:	ActiveRDF adaptor for SPARQL
Name:		ruby-activerdf_sparql
Version:	1.3.4
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/activerdf_sparql-%{version}.gem
# Source0-md5:	b2d9f0f46bef31ed1f91be9d09808849
Patch0:		%{name}-nogems.patch
Patch1:		%{name}-initfix.patch
URL:		http://activerdf.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ActiveRDF adaptor for SPARQL.

%prep
%setup -q -c
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .
%patch0 -p1
%patch1 -p1

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm ri/created.rid
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/activerdf_sparql*
%{ruby_ridir}/*
