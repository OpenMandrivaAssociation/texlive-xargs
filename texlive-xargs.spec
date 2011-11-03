# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xargs
# catalog-date 2008-08-24 00:31:24 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-xargs
Version:	1.1
Release:	1
Summary:	Define commands with many optional arguments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xargs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides extended versions of \newcommand and
related LaTeX commands, which allow easy and robust definition
of macros with many optional arguments, using a clear and
simple xkeyval-style syntax.

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
%{_texmfdistdir}/tex/latex/xargs/xargs.sty
%doc %{_texmfdistdir}/doc/latex/xargs/README
%doc %{_texmfdistdir}/doc/latex/xargs/xargs-fr.pdf
%doc %{_texmfdistdir}/doc/latex/xargs/xargs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xargs/xargs.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
