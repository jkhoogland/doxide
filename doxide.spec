Name: doxide
Version: 0.0.0
Release: 1
Summary: Modern documentation for modern C++
Vendor: Lawrence Murray <lawrence@indii.org>
License: Apache-2.0
Group: Development/Languages/C and C++
URL: https://doxide.org
Source0: %{name}-%{version}.tar.gz
BuildRequires: gcc-c++ cmake libyaml-devel

%description

Doxide generates documentation for C++ source code. It is configured with
YAML, generates Markdown, and publishes HTML. Entities in the source code are
documented with special comments containing commands, as with the classic tool
Doxygen. The source code is parsed and documentation processed into Markdown
then HTML. Doxide aims at online documentation with a modern look and
responsive design for desktop and mobile devices.

%prep
%setup -q -n %{name}-%{version}

%build
cmake -DCMAKE_BUILD_TYPE=Release . --verbose
cmake --build . --config Release --verbose %{?_smp_mflags}

%install
cmake --install . --config Release --prefix #{prefix} --verbose 

%files
%license LICENSE

%changelog
* Sat Jun 3 2023 Lawrence Murray <lawrence@indii.org> - 1:0.0.0-1
Initial setup.
