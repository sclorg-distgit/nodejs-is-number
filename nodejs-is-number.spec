%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name is-number

Summary:       Returns true if the value is a number
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.1.0
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/is-number
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Returns true if the value is a number. comprehensive tests.

To understand some of the rationale behind the decisions made 
in this library (and to learn about some oddities of number 
evaluation in JavaScript), see this gist.
https://gist.github.com/jonschlinkert/e30c70c713da325d0e81

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 2.1.0-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.1.0-1
- Initial package
