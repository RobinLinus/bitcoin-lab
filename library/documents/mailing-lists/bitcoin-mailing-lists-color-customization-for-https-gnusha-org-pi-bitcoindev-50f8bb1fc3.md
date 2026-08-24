# color customization for https://gnusha.org/pi/bitcoindev/

Source: https://gnusha.org/pi/bitcoindev/_/text/color/

Retrieved: 2026-08-24T21:52:29Z

---

public inbox for bitcoindev@googlegroups.com

help

/

color

/

mirror

/

Atom feed

color customization for

https://gnusha.org/pi/bitcoindev/

public-inbox provides a stable set of CSS classes for users to customize colors for highlighting diffs and code. Users of browsers such as dillo, Firefox, or some browser extensions may start by downloading the following sample CSS file to control the colors they see:

https://gnusha.org/pi/bitcoindev/userContent.css

CSS sample ---------- ```css /* * Firefox users: this goes in $PROFILE_FOLDER/chrome/userContent.css * where $PROFILE_FOLDER is platform-specific * * cf.

http://kb.mozillazine.org/UserContent.css

*

http://kb.mozillazine.org/Profile_folder_-_Firefox

* * Users of dillo can remove the entire lines with "moz-only" * in them and place the resulting file in ~/.dillo/style.css */ @-moz-document url-prefix(

https://gnusha.org/pi/bitcoindev/

) { /* moz-only */ /* * CC0-1.0 <

https://creativecommons.org/publicdomain/zero/1.0/legalcode

> * Dark color scheme using 216 web-safe colors, inspired * somewhat by the default color scheme in mutt. * It reduces eyestrain for me, and energy usage for all: *

https://en.wikipedia.org/wiki/Light-on-dark_color_scheme

*/ * { font-size: 100% !important; font-family: monospace !important; background:#000 !important; color:#ccc !important } pre { white-space: pre-wrap !important } /* * Underlined links add visual noise which make them hard-to-read. * Use colors to make them stand out, instead. */ a:link { color:#69f !important; text-decoration:none !important } a:visited { color:#96f !important } /* quoted text in emails gets a different color */ *.q { color:#09f !important } /* * these may be used with cgit <

https://git.zx2c4.com/cgit/

>, too. * (cgit uses <div>, public-inbox uses <span>) */ *.add { color:#0ff !important } /* diff post-image lines */ *.del { color:#f0f !important } /* diff pre-image lines */ *.head { color:#fff !important } /* diff header (metainformation) */ *.hunk { color:#c93 !important } /* diff hunk-header */ /* * highlight 3.x colors (tested 3.18) for displaying blobs. * This doesn't use most of the colors available, as I find too * many colors overwhelming, so the default is commented out. */ .hl.num { color:#f30 !important } /* number */ .hl.esc { color:#f0f !important } /* escape character */ .hl.str { color:#f30 !important } /* string */ .hl.ppc { color:#f0f !important } /* preprocessor */ .hl.pps { color:#f30 !important } /* preprocessor string */ .hl.slc { color:#09f !important } /* single-line comment */ .hl.com { color:#09f !important } /* multi-line comment */ /* .hl.opt { color:#ccc !important } */ /* operator */ /* .hl.ipl { color:#ccc !important } */ /* interpolation */ /* keyword groups kw[a-z] */ .hl.kwa { color:#ff0 !important } .hl.kwb { color:#0f0 !important } .hl.kwc { color:#ff0 !important } /* .hl.kwd { color:#ccc !important } */ /* line-number (unused by public-inbox) */ /* .hl.lin { color:#ccc !important } */ } /* moz-only */ ```

This is a public inbox, see

mirroring instructions

for how to clone and mirror all data and code used for this inbox
