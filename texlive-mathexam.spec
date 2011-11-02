Name:		texlive-mathexam
Version:	1.00
Release:	1
Summary:	Package for typesetting exams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathexam
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package can help you typeset exams (mostly in mathematics
and related disciplines where students are required to show
their calculations followed by one or more short answers). It
provides commands for inclusion of space for calculations, as
well as commands for automatic creation of "answer spaces". In
addition, the package will automatically create page headers
and footers, and will let you include instructions and space
for students to put their name.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathexam/mathexam.sty
%doc %{_texmfdistdir}/doc/latex/mathexam/README
%doc %{_texmfdistdir}/doc/latex/mathexam/mathexam.pdf
%doc %{_texmfdistdir}/doc/latex/mathexam/sample.pdf
%doc %{_texmfdistdir}/doc/latex/mathexam/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/mathexam/mathexam.dtx
%doc %{_texmfdistdir}/source/latex/mathexam/mathexam.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
