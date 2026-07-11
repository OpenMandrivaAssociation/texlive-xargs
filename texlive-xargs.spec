%global tl_name xargs
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Define commands with many optional arguments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xargs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides extended versions of \newcommand and related LaTeX
commands, which allow easy and robust definition of macros with many
optional arguments, using a clear and simple xkeyval-style syntax.

