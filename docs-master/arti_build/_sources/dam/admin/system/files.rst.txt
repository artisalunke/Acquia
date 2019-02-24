.. include:: /common/global.rst

Managing your supported file formats
====================================

You can upload, download and distribute any file format on
|acquia-product:dam|. However, admins can configure |acquia-product:dam|
to accept or exclude only specific file formats from being uploaded.

.. _configure:

Configure the Supported File Formats
------------------------------------

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings|, and then click **System
   Preferences**.
#. In the **Supported File Extensions** section, select from the
   following options, based on your requirements:

   -  **Allow certain file extensions**
   -  **Prevent certain file extensions**

#. Click **File extensions** to whitelist or blacklist certain file
   formats.
   The following values are the default for each:

   -  **Whitelist defaults** - 3d, abf, acfm, afm, ai, amfm, arw, avi,
      bdf, bmp, cha, chr, compositefont, cr2, crw, csv, dcr, dfont, dng,
      doc, docx, dotm, dotx, dst, dwg, dwx, emf, eot, eps, etx, euf,
      f3f, ffil, flv, fnt, fon, fot, gdr, gf, gif, gxf, htm, html, idml,
      iiq, ind, indd, jpeg, jpg, k25, kdc, key, lwfn, m2v, m4v, mcf,
      mef, mf, mos, mos, mov, mp3, mp4, mpeg, mpg, mrw, mxf, mxf, nef,
      nftr, numbers, ogg, orf, otf, pages, pcf, pdf, pef, pfa, pfb, pfm,
      pfr, pk, png, potx, ppt, pptx, prproj, psb, psd, pub, pxn, qxd,
      qxp, raf, rar, raw, raw, raw, raw, rtf, sfd, sfp, sit, sitx,
      sketch, sr2, srf, stl, suit, svg, svgz, swf, targa, tfm, tga, tif,
      tiff, tsv, tsv, ttc, tte, ttf, txf, txt, vfb, vlw, vnf, wav, wdtx,
      wma, wmv, woff, wpd, xfn, xft, xls, xlsx, xltx, xml, ytf, zip
   -  **Blacklist defaults** - application, aru, bat, chm, cla, class,
      cmd, com, cpl, cpl, dll, drv, ecc, exe, gadget, hta, hta, inf,
      ins, jar, js, jse, lnk, met, micro, msc, msh, msh1, msh1xml, msh2,
      msh2xml, mshxml, msi, msp, ocx, pif, ps1, ps1xml, ps2, ps2xml,
      psc1, psc2, reg, scf, scr, shs, sys, vb, vbe, vbs, vxd, ws, ws,
      wsc, wsf, wsh, xtbl

#. Enter or remove the file extensions. Separate file extensions by
   commas (for example: ``jpg, png, psd``) and do not add capitalization
   or periods.
#. If needed, you can click **Reset** to update the file extensions back
   to the default whitelisted and blacklisted file extensions.
#. Click **Save**. During the save process, |acquia-product:dam| will
   alphabetize the file format list.

.. _list:

File formats and settings
-------------------------

|acquia-product:dam| supports additional functionality for the following
media file types.

.. note::
  Previews are supported wth Multi-Media Module activated.

.. _images:

Image file types
~~~~~~~~~~~~~~~~

+-----------------+-----------------+-----------------+-----------------+
| File type       | Extension       | Preview         | In-Document     |
|                 |                 | Available\*     | Searching       |
+=================+=================+=================+=================+
| Bitmap Image    | ``.bmp``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Graphical       | ``.gif``        | |yes|           | |no|            |
| Interchange     |                 |                 |                 |
| Format File     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Joint           | ``.jpg``,       | |yes|           | |no|            |
| Photographic    | ``.jpeg``       |                 |                 |
| Experts Group   |                 |                 |                 |
| File            |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Portable        | ``.png``        | |yes|           | |no|            |
| Network Graphic |                 |                 |                 |
| File            |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Tagged Image    | ``.tif``,       | |yes|           | |no|            |
| File Format     | ``.tiff``       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _audiovideo:

Audio / video file types
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------+-----------------+-----------------+
| File type       | Extension       | Preview         | In-Document     |
|                 |                 | Available\*     | Searching       |
+=================+=================+=================+=================+
| Audio Video     | ``.avi``        | |yes|           | |no|            |
| Interleave      |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Flash Video     | ``.flv``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| MPEG Audio      | ``.mp3``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| MPEG Movie      | ``.mpg``,       | |yes|           | |no|            |
|                 | ``.mpeg``       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| MPEG-2 Video    | ``.m2v``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| MPEG-4 Video    | ``.m4v``,       | |yes|           | |no|            |
|                 | ``.mp4``        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| QuickTime Movie | ``.mov``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Targa Image     | ``.tga``,       | |yes|           | |no|            |
| File            | ``.targa``      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| WAVE Audio      | ``.wav``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Windows Media   | ``.wma``        | |yes|           | |no|            |
| Audio           |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Windows Media   | ``.wmv``        | |yes|           | |no|            |
| Video           |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _layout:

Page layout file types
~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------+-----------------+-----------------+
| File type       | Extension       | Preview         | In-Document     |
|                 |                 | Available\*     | Searching       |
+=================+=================+=================+=================+
| Encapsulated    | ``.eps``        | |yes|           | |no|            |
| PostScript File |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Illustrator     | ``.ai``         | |yes|           | |no|            |
| Vector Image    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| InDesign        | ``.ind``,       | |yes|           | |no|            |
|                 | ``.indd``       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Portable        | ``.pdf``        | |yes|           | |yes|           |
| Document Format |                 |                 | (non-secured    |
| File            |                 |                 | PDF only)       |
+-----------------+-----------------+-----------------+-----------------+
| Photoshop Image | ``.psd``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+

.. _misc:

Miscellaneous file types
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------+-----------------+-----------------+
| File type       | Extension       | Preview         | In-Document     |
|                 |                 | Available\*     | Searching       |
+=================+=================+=================+=================+
| Excel           | ``.xls``,       | |no|            | |yes|           |
|                 | ``.xlsx``       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| PowerPoint      | ``.ppt``,       | |yes|           | |yes|           |
|                 | ``.pptx``       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Word            | ``.doc``,       | |no|            | |yes|           |
|                 | ``.docx``       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Comma-Separated | ``.csv``        | |no|            | |yes|           |
| Values          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Tab-Separated   | ``.tsv``        | |no|            | |yes|           |
| Values          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Plain Text File | ``.txt``        | |no|            | |yes|           |
+-----------------+-----------------+-----------------+-----------------+
| Hypertext       | ``.htm``,       | |no|            | |yes|           |
| Markup Language | ``.html``       |                 |                 |
| File            |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _cameraraw:

Camera RAW file types
~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------+-----------------+-----------------+
| File type       | Extension       | Preview         | In-Document     |
|                 |                 | Available\*     | Searching       |
+=================+=================+=================+=================+
| Canon           | ``.cr2``,       | |yes|           | |no|            |
|                 | ``.crw``        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Contax          | ``.raw``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Fujifilm        | ``.raf``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Kodak           | ``.dcr``,       | |yes|           | |no|            |
|                 | ``.k25``,       |                 |                 |
|                 | ``.kdc``,       |                 |                 |
|                 | ``.raw``        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Konica Minolta  | ``.mrw``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Leaf            | ``.mos``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Leica           | ``.raw``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Logitech        | ``.pxn``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Mamiya          | ``.mos``,       | |yes|           | |no|            |
|                 | ``.mef``        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Nikon           | ``.nef``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Olympus         | ``.orf``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Panasonic       | ``.raw``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Pentax, Samsung | ``.pef``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Phase One       | ``.iiq``        | |yes|           | |no|            |
+-----------------+-----------------+-----------------+-----------------+
| Sony            | ``.arw``,       | |yes|           | |no|            |
|                 | ``.sr2``,       |                 |                 |
|                 | ``.srf``        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Universal       | ``.dng``        | |yes|           | |no|            |
| Camera RAW      |                 |                 |                 |
| Image Format    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
