# Created by pyp2rpm-3.3.2
%global pypi_name mando

Name:           python-%{pypi_name}
Version:        0.6.4
Release:        1%{?dist}
Summary:        Create Python CLI apps with little to no effort at all!

License:        MIT
URL:            https://mando.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(rst2ansi)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)

%description
mando: CLI interfaces for Humans! .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(rst2ansi)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
mando: CLI interfaces for Humans! .. image::

%package -n python-%{pypi_name}-doc
Summary:        mando documentation
%description -n python-%{pypi_name}-doc
Documentation for mando

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.6.4-1
- Initial package.