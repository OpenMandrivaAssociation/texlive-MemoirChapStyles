# revision 25918
# category Package
# catalog-ctan /info/latex-samples/MemoirChapStyles
# catalog-date 2012-04-11 16:14:01 +0200
# catalog-license lppl
# catalog-version 1.7e
Name:		texlive-MemoirChapStyles
Version:	1.7e
Release:	6
Summary:	Chapter styles in memoir class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-samples/MemoirChapStyles
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/MemoirChapStyles.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/MemoirChapStyles.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A showcase of chapter styles available to users of memoir: the
six provided in the class itself, plus many from elsewhere (by
the present author and others). The package's resources apply
only to memoir, but the package draws from a number of sources
relating to standard classes, including the fncychap package,
and Vincent Zoonekynd's tutorial on headings.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/MemoirChapStyles/MemoirChapStyles.pdf
%doc %{_texmfdistdir}/doc/latex/MemoirChapStyles/MemoirChapStyles.tex
%doc %{_texmfdistdir}/doc/latex/MemoirChapStyles/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7e-1
+ Revision: 804438
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7b-2
+ Revision: 753851
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.7b-1
+ Revision: 718990
- texlive-MemoirChapStyles
- texlive-MemoirChapStyles
- texlive-MemoirChapStyles
- texlive-MemoirChapStyles
- texlive-MemoirChapStyles

