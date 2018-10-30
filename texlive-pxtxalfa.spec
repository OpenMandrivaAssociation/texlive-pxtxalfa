# revision 23682
# category Package
# catalog-ctan /fonts/pxtxalfa
# catalog-date 2011-08-23 14:32:14 +0200
# catalog-license lppl
# catalog-version 1
Name:		texlive-pxtxalfa
Version:	1
Release:	12
Summary:	Virtual maths alphabets based on pxfonts and txfonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pxtxalfa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtxalfa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtxalfa.doc.tar.xz
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
%{_texmfdistdir}/fonts/map/dvips/pxtxalfa/pxtx.map
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/pxb-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/pxr-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/rtxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txb-cal.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txb-frak.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txb-of.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-cal.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-ds.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-frak.tfm
%{_texmfdistdir}/fonts/tfm/public/pxtxalfa/txr-of.tfm
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/pxb-ds.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/pxr-ds.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txb-cal.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txb-frak.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txb-of.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-cal.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-ds.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-frak.vf
%{_texmfdistdir}/fonts/vf/public/pxtxalfa/txr-of.vf
%{_texmfdistdir}/tex/latex/pxtxalfa/px-ds.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/pxtx-cal.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/pxtx-frak.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/tx-of.sty
%{_texmfdistdir}/tex/latex/pxtxalfa/upx-ds.fd
%{_texmfdistdir}/tex/latex/pxtxalfa/utx-cal.fd
%{_texmfdistdir}/tex/latex/pxtxalfa/utx-frak.fd
%{_texmfdistdir}/tex/latex/pxtxalfa/utx-of.fd
%doc %{_texmfdistdir}/doc/fonts/pxtxalfa/README
%doc %{_texmfdistdir}/doc/fonts/pxtxalfa/pxtxalfa.pdf
%doc %{_texmfdistdir}/doc/fonts/pxtxalfa/pxtxalfa.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-2
+ Revision: 755562
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 719418
- texlive-pxtxalfa
- texlive-pxtxalfa
- texlive-pxtxalfa

