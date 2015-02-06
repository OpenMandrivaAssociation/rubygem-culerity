%define oname culerity

Name:       rubygem-%{oname}
Version:    0.2.12
Release:    2
Summary:    Integrates Cucumber and Celerity in order to test your application's full stack
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/langalex/culerity
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Culerity integrates Cucumber and Celerity in order to test your application's
full stack.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/run_celerity_server.rb
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/rails/
%{ruby_gemdir}/gems/%{oname}-%{version}/rails_generators/
%{ruby_gemdir}/gems/%{oname}-%{version}/script/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/init.rb
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION.yml
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 0.2.12-1mdv2011.0
+ Revision: 623062
- oops, fix rel
- import rubygem-culerity

