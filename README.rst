Insta Meter
===========

`Build Status <https://travis-ci.org/kricha/insta_meter>`__
`PyPI <https://pypi.org/pypi/insta_meter>`__

Gather statistic for any open instagram account 📈

Examples
~~~~~~~~

-  Example of using package for getting account statistic:

   .. code:: python

      from insta_meter import InstaMeter   
      im = InstaMeter(username='al_kricha')   
      im.analyze_profile()   
      im.print_account_statistic()
      im.print_top_liked()   

   result:

   .. code:: bash

      +-- https://instagram.com/al_kricha/ --------------------------+
      |   counter                    |             value             |
      +------------------------------+-------------------------------+
      |   following                  |              229              |
      |   followed                   |              461              |
      |   posts                      |              433              |
      |   likes                      |             22830             |
      |   comments                   |             1754              |
      |   video views                |             6835              |
      |   likes/post                 |      52.725173210161664       |
      |   comments/post              |       4.05080831408776        |
      |   views/post                 |      148.58695652173913       |
      |                                                              |
      +---------- https://github.com/kricha/insta_browser -----------+
      +--------------------------------------------------------------+
      |                       top liked posts                        |
      +--------------------------------------------------------------+
      |       https://instagram.com/p/BhZDO0DBJOY/ - 139 likes       |
      |       https://instagram.com/p/BVIUvMkj1RV/ - 138 likes       |
      |       https://instagram.com/p/BTzJ38-DkUT/ - 133 likes       |
      |       https://instagram.com/p/BI8rgr-gXKg/ - 127 likes       |
      |       https://instagram.com/p/BW-I6o6DBjm/ - 121 likes       |
      |       https://instagram.com/p/BM4_XSoFhck/ - 116 likes       |
      |       https://instagram.com/p/BJVm3KIA-Vj/ - 115 likes       |
      |       https://instagram.com/p/BIhuQaCgRxI/ - 111 likes       |
      |       https://instagram.com/p/BM6XgB2l_r7/ - 110 likes       |
      |       https://instagram.com/p/BMHiRNUlHvh/ - 110 likes       |
      +--------------------------------------------------------------+
      +--------------------------------------------------------------+
      |                     top commented posts                      |
      +--------------------------------------------------------------+
      |      https://instagram.com/p/rzhgUfuPXF/ - 57 comments       |
      |      https://instagram.com/p/21L5t0OPR_/ - 29 comments       |
      |      https://instagram.com/p/BLLJRRdlIxg/ - 25 comments      |
      |      https://instagram.com/p/1LpPWhuPd4/ - 24 comments       |
      |      https://instagram.com/p/BFqgZr0OPVa/ - 23 comments      |
      |      https://instagram.com/p/BDdCroKuPdT/ - 21 comments      |
      |      https://instagram.com/p/yHxspzuPVh/ - 21 comments       |
      |      https://instagram.com/p/BKlbXDBA2zE/ - 20 comments      |
      |      https://instagram.com/p/BLWXDeuFNW3/ - 18 comments      |
      |      https://instagram.com/p/zUa94AuPet/ - 18 comments       |
      +--------------------------------------------------------------+
      +--------------------------------------------------------------+
      |                       top viewed posts                       |
      +--------------------------------------------------------------+
      |       https://instagram.com/p/BImaR7Ngwiy/ - 561 views       |
      |       https://instagram.com/p/BN1kAJMlbrv/ - 322 views       |
      |       https://instagram.com/p/BOkQ84FFeTi/ - 313 views       |
      |       https://instagram.com/p/BICnTLwAXXT/ - 305 views       |
      |       https://instagram.com/p/BKffgfvgE2U/ - 297 views       |
      |       https://instagram.com/p/BIuepnoAxsr/ - 296 views       |
      |       https://instagram.com/p/BZdIQMajT9X/ - 288 views       |
      |       https://instagram.com/p/BGJVNmhuPaY/ - 278 views       |
      |       https://instagram.com/p/BHMo02AgT7E/ - 273 views       |
      |       https://instagram.com/p/BJEJkS1Atmu/ - 263 views       |
      +--------------------------------------------------------------+
