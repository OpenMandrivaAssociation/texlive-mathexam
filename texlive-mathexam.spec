# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mathexam
# catalog-date 2008-08-22 15:19:59 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-mathexam
Version:	1.00
Release:	11
Summary:	Package for typesetting exams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathexam
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can help you typeset exams (mostly in mathematics
and related disciplines where students are required to show
their calculations followed by one or more short answers). It
provides commands for inclusion of space for calculations, as
well as commands for automatic creation of "answer spaces". In
addition, the package will automatically create page headers
and footers, and will let you include instructions and space
for students to put their name.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 753777
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 718972
- texlive-mathexam
- texlive-mathexam
- texlive-mathexam
- texlive-mathexam

