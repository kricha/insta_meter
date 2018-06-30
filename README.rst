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
      |   followed                   |              402              |
      |   posts                      |              397              |
      |   comments                   |             1602              |
      |   likes                      |             20429             |
      |   following                  |              211              |
      |   video views                |             6138              |
      |                                                              |
      +--------- https://github.com/kricha/insta_browser ------------+
      +--------------------------------------------------------------+
      |                       top liked posts                        |
      +--------------------------------------------------------------+
      |       https://instagram.com/p/BVIUvMkj1RV/ - 139 likes       |
      |       https://instagram.com/p/BTzJ38-DkUT/ - 132 likes       |
      |       https://instagram.com/p/BI8rgr-gXKg/ - 129 likes       |
      |       https://instagram.com/p/BW-I6o6DBjm/ - 119 likes       |
      |       https://instagram.com/p/BM4_XSoFhck/ - 118 likes       |
      |       https://instagram.com/p/BJVm3KIA-Vj/ - 117 likes       |
      |       https://instagram.com/p/BIhuQaCgRxI/ - 113 likes       |
      |       https://instagram.com/p/BM6XgB2l_r7/ - 112 likes       |
      |       https://instagram.com/p/BMHiRNUlHvh/ - 112 likes       |
      |       https://instagram.com/p/BLmMEwjlElP/ - 111 likes       |
      +--------------------------------------------------------------+
