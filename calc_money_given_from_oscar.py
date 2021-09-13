import re

big_string = """\
Google Domains
May 5 · Domain - juanaquino.com: 1 year renewal
-$12.00

From Mom
Apr 28
+$100.00

From Mom
Feb 16 · Miel y telefono
+$100.00

From Mom
Jan 10
+$50.00

From Mom
Nov 10, 2019
+$50.00

From Oscar Aquino
Oct 17, 2019
+$25.00

From Mom
Oct 10, 2019
+$60.00

From Oscar Aquino
Oct 9, 2019
+$25.00

From Oscar Aquino
Oct 2, 2019
+$25.00

From Oscar Aquino
Sep 25, 2019
+$25.00

From Oscar Aquino
Sep 19, 2019
+$100.00

From Oscar Aquino
Sep 19, 2019
+$25.00

From Mom
Sep 12, 2019
+$50.00

From Oscar Aquino
Sep 11, 2019
+$25.00

From Oscar Aquino
Sep 4, 2019
+$25.00

From Oscar Aquino
Aug 28, 2019
+$25.00

Google One
Aug 24, 2019 · 100 GB (Google One)
-$19.99

From Oscar Aquino
Aug 21, 2019
+$25.00

From Oscar Aquino
Aug 15, 2019
+$25.00

From Mom
Aug 10, 2019
+$72.00

From Oscar Aquino
Aug 7, 2019
+$25.00

From Oscar Aquino
Aug 1, 2019
+$25.00

From Oscar Aquino
Jul 25, 2019
+$25.00

From Oscar Aquino
Jul 17, 2019
+$25.00

From Mom
Jul 11, 2019 · Para telefono hijo
+$50.00

From Oscar Aquino
Jul 10, 2019
+$25.00

From Oscar Aquino
Jul 2, 2019
+$25.00

From Mom
Jun 27, 2019
+$125.00

From Oscar Aquino
Jun 26, 2019
+$25.00

From Oscar Aquino
Jun 20, 2019
+$25.00

From Oscar Aquino
Jun 12, 2019
+$25.00

From Mom
Jun 10, 2019
+$50.00

From Oscar Aquino
Jun 5, 2019
+$25.00

From Oscar Aquino
May 30, 2019
+$25.00

From Oscar Aquino
May 22, 2019
+$25.00

From Oscar Aquino
May 15, 2019
+$25.00

From Mom
May 10, 2019
+$65.00

From Oscar Aquino
May 9, 2019
+$25.00

Google Domains
May 5, 2019 · Domain - juanaquino.com: 1 year renewal
-$12.00

From Oscar Aquino
May 1, 2019
+$25.00

From Oscar Aquino
Apr 24, 2019
+$25.00

From Oscar Aquino
Apr 17, 2019
+$25.00

From Oscar Aquino
Apr 10, 2019
+$25.00

From Oscar Aquino
Apr 3, 2019
+$25.00

From Mom
Apr 3, 2019
+$96.00

From Oscar Aquino
Mar 28, 2019
+$25.00

From Oscar Aquino
Mar 20, 2019
+$25.00

From Oscar Aquino
Mar 13, 2019
+$25.00

From Oscar Aquino
Mar 7, 2019
+$25.00

From Oscar Aquino
Feb 27, 2019
+$25.00

From Mom
Feb 23, 2019
+$60.00

From Oscar Aquino
Feb 20, 2019
+$25.00

From Oscar Aquino
Feb 13, 2019
+$25.00

From Mom
Feb 11, 2019
+$80.00

From Oscar Aquino
Feb 6, 2019
+$25.00

From Oscar Aquino
Jan 30, 2019
+$25.00

Google Play Apps
Jan 25, 2019 · My Boy! - GBA Emulator
-$4.99

From Oscar Aquino
Jan 23, 2019
+$25.00

From Oscar Aquino
Jan 16, 2019
+$25.00

From Oscar Aquino
Jan 5, 2019 · For christmas
+$94.00

From Oscar Aquino
Jan 2, 2019 · 8===D
+$25.00

From Oscar Aquino
Dec 26, 2018
+$25.00

From Oscar Aquino
Dec 19, 2018
+$25.00

From Mom
Dec 17, 2018
+$10.00

From Oscar Aquino
Dec 12, 2018
+$25.00

To Oscar Aquino
Dec 6, 2018 · to help out with umbrella
-$10.00

From Oscar Aquino
Dec 5, 2018
+$25.00

From Oscar Aquino
Nov 28, 2018
+$25.00

From Oscar Aquino
Nov 21, 2018
+$25.00

Google Play Apps
Nov 20, 2018 · Monument Valley
-$0.99

Google Play Apps
Nov 20, 2018 · Monument Valley 2
-$0.99

Google Shopping
Nov 19, 2018 · Google Shopping, Google Shopping
-$42.18

From Mom
Nov 17, 2018
+$60.00

Google Play Apps
Nov 17, 2018 · Pro (Custom Navigation Bar)
-$1.99

From Oscar Aquino
Nov 15, 2018
+$25.00

From Oscar Aquino
Nov 8, 2018
+$25.00

From Mom
Nov 7, 2018
+$170.00

From Oscar Aquino
Nov 5, 2018 · 8====D
+$6.18

From Oscar Aquino
Oct 31, 2018
+$25.00

From Mom
Oct 25, 2018
+$10.00

From Oscar Aquino
Oct 24, 2018 · 8===D
+$25.00

From Oscar Aquino
Oct 17, 2018
+$25.00

From Oscar Aquino
Oct 10, 2018
+$25.00

From Oscar Aquino
Oct 3, 2018
+$25.00

From Mom
Sep 28, 2018
+$140.00

From Oscar Aquino
Sep 26, 2018 · 8==D
+$25.00

From Oscar Aquino
Sep 19, 2018
+$25.00

From Oscar Aquino
Sep 13, 2018
+$25.00

From Oscar Aquino
Sep 6, 2018
+$25.00

From Oscar Aquino
Aug 29, 2018
+$25.00

Google Play Apps
Aug 24, 2018 · AutoInput (AutoApps)
-$1.99

Google Play Apps
Aug 24, 2018 · AutoVoice (AutoApps)
-$2.99

Google One
Aug 24, 2018 · 100 GB (Google One)
-$19.99

From Oscar Aquino
Aug 22, 2018
+$25.00

From Oscar Aquino
Aug 16, 2018 · 8==D
+$25.00

From Mom
Aug 11, 2018
+$42.00

From Oscar Aquino
Aug 8, 2018 · 8===D
+$25.00

From Oscar Aquino
Aug 3, 2018
+$25.00

From Oscar Aquino
Jul 27, 2018
+$25.00

Google Domains
Apr 28, 2018 · Domain - juanaquino.com: 1 year renewal
-$12.00

Google Play Apps
Apr 15, 2018 · Status Bar Mini PRO
-$1.00

Google Play Apps
Apr 15, 2018 · AutoTools (AutoApps)
-$2.99

Google Play Apps
Apr 15, 2018 · Tasker
-$2.99

From Mom
Mar 27, 2018
+$30.00

Google Shopping
Mar 21, 2018 · Google Express, Google Express
-$29.73

Google Shopping
Mar 19, 2018 · Google Express, Google Express
$0.00
Refunded

From Mom
Mar 18, 2018
+$45.00

From Mom
Mar 10, 2018
+$107.00

Google Play Apps
Mar 3, 2018 · Sync for reddit (Pro)
$0.00
Refunded

Google Play Apps
Feb 26, 2018 · GMD Immersive PRO key (GMD Full Screen Immersive Mode)
-$3.55

From Mom
Feb 21, 2018
+$40.00

Google Play Apps
Feb 19, 2018 · Add reminder to Google Now
-$1.00

From Mom
Feb 5, 2018
+$60.00

From Mom
Dec 30, 2017
+$42.00

Google Play Apps
Dec 26, 2017 · Full Version Unlock (Solid Explorer File Manager)
-$0.99\
"""

first_part = """\
From Oscar Aquino
Oct 17, 2019
+$25.00

From Mom
Oct 10, 2019
+$60.00

From Oscar Aquino
Oct 9, 2019
+$25.00

From Oscar Aquino
Oct 2, 2019
+$25.00

From Oscar Aquino
Sep 25, 2019
+$25.00

From Oscar Aquino
Sep 19, 2019
+$100.00

From Oscar Aquino
Sep 19, 2019
+$25.00

From Mom
Sep 12, 2019
+$50.00

From Oscar Aquino
Sep 11, 2019
+$25.00

From Oscar Aquino
Sep 4, 2019
+$25.00

From Oscar Aquino
Aug 28, 2019
+$25.00

Google One
Aug 24, 2019 · 100 GB (Google One)
-$19.99

From Oscar Aquino
Aug 21, 2019
+$25.00

From Oscar Aquino
Aug 15, 2019
+$25.00

From Mom
Aug 10, 2019
+$72.00

From Oscar Aquino
Aug 7, 2019
+$25.00

From Oscar Aquino
Aug 1, 2019
+$25.00

From Oscar Aquino
Jul 25, 2019
+$25.00

From Oscar Aquino
Jul 17, 2019
+$25.00

From Mom
Jul 11, 2019 · Para telefono hijo
+$50.00

From Oscar Aquino
Jul 10, 2019
+$25.00

From Oscar Aquino
Jul 2, 2019
+$25.00

From Mom
Jun 27, 2019
+$125.00

From Oscar Aquino
Jun 26, 2019
+$25.00

From Oscar Aquino
Jun 20, 2019
+$25.00

From Oscar Aquino
Jun 12, 2019
+$25.00

From Mom
Jun 10, 2019
+$50.00

From Oscar Aquino
Jun 5, 2019
+$25.00

From Oscar Aquino
May 30, 2019
+$25.00

From Oscar Aquino
May 22, 2019
+$25.00

From Oscar Aquino
May 15, 2019
+$25.00

From Mom
May 10, 2019
+$65.00

From Oscar Aquino
May 9, 2019
+$25.00

Google Domains
May 5, 2019 · Domain - juanaquino.com: 1 year renewal
-$12.00

From Oscar Aquino
May 1, 2019
+$25.00\
"""

second_part = """\
From Oscar Aquino
Apr 24, 2019
+$25.00

From Oscar Aquino
Apr 17, 2019
+$25.00

From Oscar Aquino
Apr 10, 2019
+$25.00

From Oscar Aquino
Apr 3, 2019
+$25.00

From Mom
Apr 3, 2019
+$96.00

From Oscar Aquino
Mar 28, 2019
+$25.00

From Oscar Aquino
Mar 20, 2019
+$25.00

From Oscar Aquino
Mar 13, 2019
+$25.00

From Oscar Aquino
Mar 7, 2019
+$25.00

From Oscar Aquino
Feb 27, 2019
+$25.00

From Mom
Feb 23, 2019
+$60.00

From Oscar Aquino
Feb 20, 2019
+$25.00

From Oscar Aquino
Feb 13, 2019
+$25.00

From Mom
Feb 11, 2019
+$80.00

From Oscar Aquino
Feb 6, 2019
+$25.00

From Oscar Aquino
Jan 30, 2019
+$25.00

Google Play Apps
Jan 25, 2019 · My Boy! - GBA Emulator
-$4.99

From Oscar Aquino
Jan 23, 2019
+$25.00

From Oscar Aquino
Jan 16, 2019
+$25.00

From Oscar Aquino
Jan 5, 2019 · For christmas
+$94.00\
"""

third_part = """\
From Oscar Aquino
Jan 2, 2019 · 8===D
+$25.00

From Oscar Aquino
Dec 26, 2018
+$25.00

From Oscar Aquino
Dec 19, 2018
+$25.00

From Mom
Dec 17, 2018
+$10.00

From Oscar Aquino
Dec 12, 2018
+$25.00

To Oscar Aquino
Dec 6, 2018 · to help out with umbrella
-$10.00

From Oscar Aquino
Dec 5, 2018
+$25.00

From Oscar Aquino
Nov 28, 2018
+$25.00

From Oscar Aquino
Nov 21, 2018
+$25.00

Google Play Apps
Nov 20, 2018 · Monument Valley
-$0.99

Google Play Apps
Nov 20, 2018 · Monument Valley 2
-$0.99

Google Shopping
Nov 19, 2018 · Google Shopping, Google Shopping
-$42.18

From Mom
Nov 17, 2018
+$60.00

Google Play Apps
Nov 17, 2018 · Pro (Custom Navigation Bar)
-$1.99

From Oscar Aquino
Nov 15, 2018
+$25.00

From Oscar Aquino
Nov 8, 2018
+$25.00

From Mom
Nov 7, 2018
+$170.00

From Oscar Aquino
Nov 5, 2018 · 8====D
+$6.18

From Oscar Aquino
Oct 31, 2018
+$25.00\
"""

fourth_part = """\
From Oscar Aquino
Oct 24, 2018 · 8===D
+$25.00

From Oscar Aquino
Oct 17, 2018
+$25.00

From Oscar Aquino
Oct 10, 2018
+$25.00

From Oscar Aquino
Oct 3, 2018
+$25.00

From Mom
Sep 28, 2018
+$140.00

From Oscar Aquino
Sep 26, 2018 · 8==D
+$25.00

From Oscar Aquino
Sep 19, 2018
+$25.00

From Oscar Aquino
Sep 13, 2018
+$25.00

From Oscar Aquino
Sep 6, 2018
+$25.00

From Oscar Aquino
Aug 29, 2018
+$25.00

Google Play Apps
Aug 24, 2018 · AutoInput (AutoApps)
-$1.99

Google Play Apps
Aug 24, 2018 · AutoVoice (AutoApps)
-$2.99

Google One
Aug 24, 2018 · 100 GB (Google One)
-$19.99

From Oscar Aquino
Aug 22, 2018
+$25.00

From Oscar Aquino
Aug 16, 2018 · 8==D
+$25.00

From Mom
Aug 11, 2018
+$42.00

From Oscar Aquino
Aug 8, 2018 · 8===D
+$25.00

From Oscar Aquino
Aug 3, 2018
+$25.00

From Oscar Aquino
Jul 27, 2018
+$25.00\
"""

fifth_part = """\
Google Play Apps
Apr 15, 2018 · Status Bar Mini PRO
-$1.00

Google Play Apps
Apr 15, 2018 · AutoTools (AutoApps)
-$2.99

Google Play Apps
Apr 15, 2018 · Tasker
-$2.99

From Mom
Mar 27, 2018
+$30.00

Google Shopping
Mar 21, 2018 · Google Express, Google Express
-$29.73

Google Shopping
Mar 19, 2018 · Google Express, Google Express
$0.00
Refunded

From Mom
Mar 18, 2018
+$45.00

From Mom
Mar 10, 2018
+$107.00

Google Play Apps
Mar 3, 2018 · Sync for reddit (Pro)
$0.00
Refunded

Google Play Apps
Feb 26, 2018 · GMD Immersive PRO key (GMD Full Screen Immersive Mode)
-$3.55

From Mom
Feb 21, 2018
+$40.00

Google Play Apps
Feb 19, 2018 · Add reminder to Google Now
-$1.00

From Mom
Feb 5, 2018
+$60.00

From Mom
Dec 30, 2017
+$42.00

Google Play Apps
Dec 26, 2017 · Full Version Unlock (Solid Explorer File Manager)
-$0.99

Google Play Apps
Dec 25, 2017 · MX Player Pro
-$5.99

Google Shopping
Dec 23, 2017 · Google Express, Google Express
-$3.26

From Mom
Dec 12, 2017
+$50.00

From Mom
Nov 26, 2017
+$35.00

To Jesse Kirkpatrick
Nov 6, 2017
-$6.00

To Jesse Kirkpatrick
Nov 4, 2017 · 🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏
-$5.00

From Mom
Oct 9, 2017
+$40.00

From Oscar Aquino
Sep 4, 2017 · 8====D
+$20.00

From Mom
Sep 2, 2017
+$25.00

From Mom
Jul 31, 2017
+$30.00

From Oscar Aquino
Jul 26, 2017
+$20.00

From Oscar Aquino
Jun 30, 2017 · 8=====D
+$20.00

From Mom
Jun 30, 2017
+$25.00

Google Play Apps
May 30, 2017 · Remove Ads (Relay for reddit)
-$2.99

From Oscar Aquino
May 27, 2017
+$20.00

To Oscar Aquino
May 27, 2017
-$1.00

From Rosario Saban
May 27, 2017 · hey juan aqui esta el dinero
+$60.00

To Rosario Saban
May 27, 2017 · Hola ma
-$1.00
Canceled

To Oscar Aquino
May 27, 2017 · Hello
-$1.00
Canceled

Google Play Apps
May 22, 2017 · Greenify (Donation Package)
-$2.99

Google Domains
May 5, 2017 · Domain - juanaquino.com
-$12.00

To Oscar Aquino
Mar 15, 2017 · 🎺🎺🎺
-$1.00
Canceled

Google Store
Feb 13, 2017 · Chromecast (Black), $5 Off Chromecast/Chromecast Audio
-$32.62

Google Play Movies
Nov 24, 2016 · High School DxD, Season 1
-$1.00

Google Play Apps
Aug 29, 2016 · Lux Auto Brightness
-$3.80\
"""

full_page_string = """\
Google Domains
May 5 · Domain - juanaquino.com: 1 year renewal
-$12.00

From Mom
Apr 28
+$100.00

From Mom
Feb 16 · Miel y telefono
+$100.00

From Mom
Jan 10
+$50.00

From Mom
Nov 10, 2019
+$50.00

From Oscar Aquino
Oct 17, 2019
+$25.00

From Mom
Oct 10, 2019
+$60.00

From Oscar Aquino
Oct 9, 2019
+$25.00

From Oscar Aquino
Oct 2, 2019
+$25.00

From Oscar Aquino
Sep 25, 2019
+$25.00

From Oscar Aquino
Sep 19, 2019
+$100.00

From Oscar Aquino
Sep 19, 2019
+$25.00

From Mom
Sep 12, 2019
+$50.00

From Oscar Aquino
Sep 11, 2019
+$25.00

From Oscar Aquino
Sep 4, 2019
+$25.00

From Oscar Aquino
Aug 28, 2019
+$25.00

Google One
Aug 24, 2019 · 100 GB (Google One)
-$19.99

From Oscar Aquino
Aug 21, 2019
+$25.00

From Oscar Aquino
Aug 15, 2019
+$25.00

From Mom
Aug 10, 2019
+$72.00

From Oscar Aquino
Aug 7, 2019
+$25.00

From Oscar Aquino
Aug 1, 2019
+$25.00

From Oscar Aquino
Jul 25, 2019
+$25.00

From Oscar Aquino
Jul 17, 2019
+$25.00

From Mom
Jul 11, 2019 · Para telefono hijo
+$50.00

From Oscar Aquino
Jul 10, 2019
+$25.00

From Oscar Aquino
Jul 2, 2019
+$25.00

From Mom
Jun 27, 2019
+$125.00

From Oscar Aquino
Jun 26, 2019
+$25.00

From Oscar Aquino
Jun 20, 2019
+$25.00

From Oscar Aquino
Jun 12, 2019
+$25.00

From Mom
Jun 10, 2019
+$50.00

From Oscar Aquino
Jun 5, 2019
+$25.00

From Oscar Aquino
May 30, 2019
+$25.00

From Oscar Aquino
May 22, 2019
+$25.00

From Oscar Aquino
May 15, 2019
+$25.00

From Mom
May 10, 2019
+$65.00

From Oscar Aquino
May 9, 2019
+$25.00

Google Domains
May 5, 2019 · Domain - juanaquino.com: 1 year renewal
-$12.00

From Oscar Aquino
May 1, 2019
+$25.00

From Oscar Aquino
Apr 24, 2019
+$25.00

From Oscar Aquino
Apr 17, 2019
+$25.00

From Oscar Aquino
Apr 10, 2019
+$25.00

From Oscar Aquino
Apr 3, 2019
+$25.00

From Mom
Apr 3, 2019
+$96.00

From Oscar Aquino
Mar 28, 2019
+$25.00

From Oscar Aquino
Mar 20, 2019
+$25.00

From Oscar Aquino
Mar 13, 2019
+$25.00

From Oscar Aquino
Mar 7, 2019
+$25.00

From Oscar Aquino
Feb 27, 2019
+$25.00

From Mom
Feb 23, 2019
+$60.00

From Oscar Aquino
Feb 20, 2019
+$25.00

From Oscar Aquino
Feb 13, 2019
+$25.00

From Mom
Feb 11, 2019
+$80.00

From Oscar Aquino
Feb 6, 2019
+$25.00

From Oscar Aquino
Jan 30, 2019
+$25.00

Google Play Apps
Jan 25, 2019 · My Boy! - GBA Emulator
-$4.99

From Oscar Aquino
Jan 23, 2019
+$25.00

From Oscar Aquino
Jan 16, 2019
+$25.00

From Oscar Aquino
Jan 5, 2019 · For christmas
+$94.00

From Oscar Aquino
Jan 2, 2019 · 8===D
+$25.00

From Oscar Aquino
Dec 26, 2018
+$25.00

From Oscar Aquino
Dec 19, 2018
+$25.00

From Mom
Dec 17, 2018
+$10.00

From Oscar Aquino
Dec 12, 2018
+$25.00

To Oscar Aquino
Dec 6, 2018 · to help out with umbrella
-$10.00

From Oscar Aquino
Dec 5, 2018
+$25.00

From Oscar Aquino
Nov 28, 2018
+$25.00

From Oscar Aquino
Nov 21, 2018
+$25.00

Google Play Apps
Nov 20, 2018 · Monument Valley
-$0.99

Google Play Apps
Nov 20, 2018 · Monument Valley 2
-$0.99

Google Shopping
Nov 19, 2018 · Google Shopping, Google Shopping
-$42.18

From Mom
Nov 17, 2018
+$60.00

Google Play Apps
Nov 17, 2018 · Pro (Custom Navigation Bar)
-$1.99

From Oscar Aquino
Nov 15, 2018
+$25.00

From Oscar Aquino
Nov 8, 2018
+$25.00

From Mom
Nov 7, 2018
+$170.00

From Oscar Aquino
Nov 5, 2018 · 8====D
+$6.18

From Oscar Aquino
Oct 31, 2018
+$25.00

From Mom
Oct 25, 2018
+$10.00

From Oscar Aquino
Oct 24, 2018 · 8===D
+$25.00

From Oscar Aquino
Oct 17, 2018
+$25.00

From Oscar Aquino
Oct 10, 2018
+$25.00

From Oscar Aquino
Oct 3, 2018
+$25.00

From Mom
Sep 28, 2018
+$140.00

From Oscar Aquino
Sep 26, 2018 · 8==D
+$25.00

From Oscar Aquino
Sep 19, 2018
+$25.00

From Oscar Aquino
Sep 13, 2018
+$25.00

From Oscar Aquino
Sep 6, 2018
+$25.00

From Oscar Aquino
Aug 29, 2018
+$25.00

Google Play Apps
Aug 24, 2018 · AutoInput (AutoApps)
-$1.99

Google Play Apps
Aug 24, 2018 · AutoVoice (AutoApps)
-$2.99

Google One
Aug 24, 2018 · 100 GB (Google One)
-$19.99

From Oscar Aquino
Aug 22, 2018
+$25.00

From Oscar Aquino
Aug 16, 2018 · 8==D
+$25.00

From Mom
Aug 11, 2018
+$42.00

From Oscar Aquino
Aug 8, 2018 · 8===D
+$25.00

From Oscar Aquino
Aug 3, 2018
+$25.00

From Oscar Aquino
Jul 27, 2018
+$25.00

Google Domains
Apr 28, 2018 · Domain - juanaquino.com: 1 year renewal
-$12.00

Google Play Apps
Apr 15, 2018 · Status Bar Mini PRO
-$1.00

Google Play Apps
Apr 15, 2018 · AutoTools (AutoApps)
-$2.99

Google Play Apps
Apr 15, 2018 · Tasker
-$2.99

From Mom
Mar 27, 2018
+$30.00

Google Shopping
Mar 21, 2018 · Google Express, Google Express
-$29.73

Google Shopping
Mar 19, 2018 · Google Express, Google Express
$0.00
Refunded

From Mom
Mar 18, 2018
+$45.00

From Mom
Mar 10, 2018
+$107.00

Google Play Apps
Mar 3, 2018 · Sync for reddit (Pro)
$0.00
Refunded

Google Play Apps
Feb 26, 2018 · GMD Immersive PRO key (GMD Full Screen Immersive Mode)
-$3.55

From Mom
Feb 21, 2018
+$40.00

Google Play Apps
Feb 19, 2018 · Add reminder to Google Now
-$1.00

From Mom
Feb 5, 2018
+$60.00

From Mom
Dec 30, 2017
+$42.00

Google Play Apps
Dec 26, 2017 · Full Version Unlock (Solid Explorer File Manager)
-$0.99

Google Play Apps
Dec 25, 2017 · MX Player Pro
-$5.99

Google Shopping
Dec 23, 2017 · Google Express, Google Express
-$3.26

From Mom
Dec 12, 2017
+$50.00

From Mom
Nov 26, 2017
+$35.00

To Jesse Kirkpatrick
Nov 6, 2017
-$6.00

To Jesse Kirkpatrick
Nov 4, 2017 · 🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏
-$5.00

From Mom
Oct 9, 2017
+$40.00

From Oscar Aquino
Sep 4, 2017 · 8====D
+$20.00

From Mom
Sep 2, 2017
+$25.00

From Mom
Jul 31, 2017
+$30.00

From Oscar Aquino
Jul 26, 2017
+$20.00

From Oscar Aquino
Jun 30, 2017 · 8=====D
+$20.00

From Mom
Jun 30, 2017
+$25.00

Google Play Apps
May 30, 2017 · Remove Ads (Relay for reddit)
-$2.99

From Oscar Aquino
May 27, 2017
+$20.00

To Oscar Aquino
May 27, 2017
-$1.00

From Rosario Saban
May 27, 2017 · hey juan aqui esta el dinero
+$60.00

To Rosario Saban
May 27, 2017 · Hola ma
-$1.00
Canceled

To Oscar Aquino
May 27, 2017 · Hello
-$1.00
Canceled

Google Play Apps
May 22, 2017 · Greenify (Donation Package)
-$2.99

Google Domains
May 5, 2017 · Domain - juanaquino.com
-$12.00

To Oscar Aquino
Mar 15, 2017 · 🎺🎺🎺
-$1.00
Canceled

Google Store
Feb 13, 2017 · Chromecast (Black), $5 Off Chromecast/Chromecast Audio
-$32.62

Google Play Movies
Nov 24, 2016 · High School DxD, Season 1
-$1.00

Google Play Apps
Aug 29, 2016 · Lux Auto Brightness
-$3.80

Google Play Apps
Aug 29, 2016 · EX Kernel Manager
-$3.99

Google Play Apps
Aug 17, 2016 · Plex for Android Activation (Plex for Android)
-$4.99

Google Play Apps
Jul 26, 2016 · Stopwatch & Timer+
-$2.99

Google Play Devices
Jul 25, 2016 · Google Cardboard (Single)
-$16.35

Google Play Devices
Jul 20, 2016 · Nexus 5X (16GB, Quartz)
-$216.91

Google Play Apps
Jul 12, 2016 · 550 PokéCoins (Pokémon GO)
-$4.99

Google Play Apps
Jul 12, 2016 · 550 PokéCoins (Pokémon GO)
-$4.99

YouTube Movies
May 24, 2016 · The Hadza: Last of the First
-$9.99

YouTube Movies
May 22, 2016 · YouTube Red
-$0.99

YouTube Movies
May 18, 2016 · The Hadza: Last of the First
-$4.99

Google Play Apps
Apr 28, 2016 · Sleep as Android Unlock
-$3.99

Google Voice
Mar 21, 2015 · Google Voice port in number (562) 639-6804
-$20.00

Google Voice
Mar 21, 2015 · Google Voice
+$20.00
Refunded

Google Voice
Mar 20, 2015 · Google Voice port in number (562) 639-6804
-$20.00

Google Play Apps
Nov 29, 2014 · Poweramp Full Version Unlocker
-$0.99

Google Play Apps
Oct 16, 2014 · Sleep Cycle alarm clock
-$0.99

Google Play Books
May 3, 2012 · Google Play Books
-$11.99\
"""

def print_total_received(payments_string):
    total_received = 0
    payments_received = 0
    for i, section in enumerate(payments_string.split("\n\n")):
        lines = section.split("\n")
        source = lines[0]
        date = lines[1]
        payment = lines[2]
        payment = int(re.search(r"\d+", payment)[0])

        if "From Oscar Aquino" in source:
            total_received += payment
            payments_received += 1

            # print()
            # print(section)
            # print()
    print(f"{total_received=} {payments_received=}")

    return total_received


total_sum_received = 0
total_sum_received += print_total_received(first_part)
total_sum_received += print_total_received(second_part)
total_sum_received += print_total_received(third_part)
total_sum_received += print_total_received(fourth_part)
total_sum_received += print_total_received(fifth_part)  # its debatable whether this should count as it seems to old (payments from 2017)

print(f"{total_sum_received=}")

print_total_received(big_string) # should be 1800
print_total_received(full_page_string) #  should be 1880, 80 of which is debatably too old (from 2017) to count