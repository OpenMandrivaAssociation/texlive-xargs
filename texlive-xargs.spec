Name:		texlive-xargs
Version:	15878
Release:	1
Summary:	Define commands with many optional arguments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xargs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides extended versions of \newcommand and
related LaTeX commands, which allow easy and robust definition
of macros with many optional arguments, using a clear and
simple xkeyval-style syntax.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xargs/xargs.sty
%doc %{_texmfdistdir}/doc/latex/xargs/README
%doc %{_texmfdistdir}/doc/latex/xargs/xargs-fr.pdf
%doc %{_texmfdistdir}/doc/latex/xargs/xargs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xargs/xargs.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
