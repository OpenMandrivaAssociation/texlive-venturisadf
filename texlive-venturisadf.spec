%global tl_name venturisadf
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Venturis ADF fonts collection
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/venturisadf
License:	lppl1.3 other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/venturisadf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/venturisadf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/venturisadf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Serif and sans serif complete text font families, in both Adobe Type 1
and OpenType formats for publication. The family is based on Utopia
family, and has been modified and developed by the Arkandis Digital
foundry. Support for using the fonts, in LaTeX, is also provided (and
makes use of the nfssext-cfr package).

