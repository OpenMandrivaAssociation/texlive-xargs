# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xargs
# catalog-date 2008-08-24 00:31:24 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-xargs
Version:	1.1
Release:	3
Summary:	Define commands with many optional arguments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xargs
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xargs.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757547
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719915
- texlive-xargs
- texlive-xargs
- texlive-xargs

