# revision 18249
# category Package
# catalog-ctan /info/latex-samples/MemoirChapStyles
# catalog-date 2010-05-10 13:49:50 +0200
# catalog-license lppl
# catalog-version 1.7b
Name:		texlive-MemoirChapStyles
Version:	1.7b
Release:	1
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
