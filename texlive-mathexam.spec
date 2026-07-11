%global tl_name mathexam
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.00
Release:	%{tl_revision}.1
Summary:	Package for typesetting exams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathexam
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathexam.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can help you typeset exams (mostly in mathematics and
related disciplines where students are required to show their
calculations followed by one or more short answers). It provides
commands for inclusion of space for calculations, as well as commands
for automatic creation of "answer spaces". In addition, the package will
automatically create page headers and footers, and will let you include
instructions and space for students to put their name.

