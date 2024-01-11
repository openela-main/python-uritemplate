%global modname uritemplate
%global altname uritemplate.py

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        3.0.0
Release:        3%{?dist}
Summary:        Simple python library to deal with URI Templates (RFC 6570)

License:        BSD
URL:            https://%{modname}.readthedocs.io
Source0:        https://github.com/sigmavirus24/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
Conflicts:      python3-uri-templates
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n uritemplate-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v

%files -n python3-%{modname}
%license LICENSE
%doc HISTORY.rst README.rst
%{python3_sitelib}/%{modname}-*.egg-info
%{python3_sitelib}/%{modname}/

%changelog
* Wed Jun 13 2018 Petr Viktorin <pviktori@redhat.com> - 3.0.0-3
- Remove the Python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Nick Bebout <nb@fedoraproject.org> - 3.0.0-1
- Upgrade to 3.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-1
- Initial package
