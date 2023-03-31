Name:		texlive-pxtxalfa
Version:	60847
Release:	2
Summary:	Virtual maths alphabets based on pxfonts and txfonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pxtxalfa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtxalfa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtxalfa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides virtual math alphabets based on pxfonts
and txfonts, with LaTeX support files and adjusted metrics. The
mathalfa package offers support for this collection.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
#{_texmfdistdir}/fonts/map/dvips/pxtxalfa
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa
%{_texmfdistdir}/fonts/vf/public/pxtxalfa
%{_texmfdistdir}/tex/latex/pxtxalfa
%doc %{_texmfdistdir}/doc/fonts/pxtxalfa

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
