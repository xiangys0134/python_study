#!/usr/bin/python
# -*- coding: utf-8 -*-

a = {"/data/www/gmf_utility": {"last_commited": "2018-11-16 14:55:11 +08:00", "oid": "a07fdaaab797f9b452cef672194ca27bc8771734", "branch": "develop"}, "/data/www/gmf_front": {"last_commited": "2018-12-19 09:21:16 +08:00", "oid": "32b0d1e38a629396ea936ee6846b53ecbcec82d9", "branch": "feature/waimao3.28.1_15"}, "/data/www/gmf_rms": {"last_commited": "2018-11-23 13:55:04 +08:00", "oid": "718c5ca768824f346fccf3ade980608d744de76e", "branch": "master"}, "/data/www/gmf_oms": {"last_commited": "2018-12-18 16:10:18 +08:00", "oid": "78fac2f4e38ba9060b7e8515a641ebe585e8d9b7", "branch": "WM_branch"}, "/data/www/xc-pms": {"last_commited": "2018-12-14 20:26:15 +08:00", "oid": "1bd420f8e3aad244bd345b8fc2ef46f64cd25149", "branch": "master"}, "/data/www/gmf_irs": {"last_commited": "2018-10-27 09:44:11 +08:00", "oid": "99c12f2384edbd6dbbeadb143570dc17ae8fa1ed", "branch": "master"}, "/data/www/xc-uds": {"last_commited": "2018-12-18 20:37:14 +08:00", "oid": "909b34bbc406115510b05ee30dfe113e6bd8fb77", "branch": "WM_branch"}, "/data/www/gmf_bms": {"last_commited": "2018-12-18 20:23:03 +08:00", "oid": "e805c6f3fef396266fb3012c7b56201ff5bc4224", "branch": "WM_branch"}, "/data/www/gmf_ipb": {"last_commited": "2018-12-18 10:10:04 +08:00", "oid": "b127e0ef14d1d7ff02c5727aba6ab498d6e52f9a", "branch": "master"}}
b = {"/data/www/gmf_utility": {"last_commited": "2018-12-06 20:21:18 +08:00", "oid": "3f6dcdb7214ad83becef9413058b4941650efb72", "branch": "HEAD"}, "/data/www/gmf_front": {"last_commited": "2018-12-19 09:21:20 +08:00", "oid": "32b0d1e38a629396ea936ee6846b53ecbcec82d9", "branch": "feature/waimao3.28.1_15"}, "/data/www/gmf_rms": {"last_commited": "2018-12-06 20:21:17 +08:00", "oid": "c1d2aaf3c1f2320aa038257460cd6962f97c193c", "branch": "HEAD"}, "/data/www/gmf_oms": {"last_commited": "2018-12-18 16:10:20 +08:00", "oid": "78fac2f4e38ba9060b7e8515a641ebe585e8d9b7", "branch": "WM_branch"}, "/data/www/xc-pms": {"last_commited": "2018-12-06 20:21:18 +08:00", "oid": "6f8152d971e12d88308f2246459472b102ca8abf", "branch": "HEAD"}, "/data/www/gmf_irs": {"last_commited": "2018-12-06 20:21:01 +08:00", "oid": "99c12f2384edbd6dbbeadb143570dc17ae8fa1ed", "branch": "HEAD"}, "/data/www/xc-uds": {"last_commited": "2018-12-18 20:37:35 +08:00", "oid": "909b34bbc406115510b05ee30dfe113e6bd8fb77", "branch": "WM_branch"}, "/data/www/gmf_bms": {"last_commited": "2018-12-18 20:23:06 +08:00", "oid": "e805c6f3fef396266fb3012c7b56201ff5bc4224", "branch": "WM_branch"}, "/data/www/gmf_ipb": {"last_commited": "2018-12-06 20:20:55 +08:00", "oid": "950b44fef25a10c558c0718a11392833d659d7a7", "branch": "HEAD"}}
c = {"/data/www/gmf_utility": {"last_commited": "2018-12-06 20:30:02 +08:00", "oid": "3f6dcdb7214ad83becef9413058b4941650efb72", "branch": "HEAD"}, "/data/www/gmf_front": {"last_commited": "2018-12-19 09:21:20 +08:00", "oid": "32b0d1e38a629396ea936ee6846b53ecbcec82d9", "branch": "feature/waimao3.28.1_15"}, "/data/www/gmf_rms": {"last_commited": "2018-12-06 20:30:02 +08:00", "oid": "c1d2aaf3c1f2320aa038257460cd6962f97c193c", "branch": "HEAD"}, "/data/www/gmf_oms": {"last_commited": "2018-12-18 16:10:22 +08:00", "oid": "78fac2f4e38ba9060b7e8515a641ebe585e8d9b7", "branch": "WM_branch"}, "/data/www/xc-pms": {"last_commited": "2018-12-06 20:30:02 +08:00", "oid": "6f8152d971e12d88308f2246459472b102ca8abf", "branch": "HEAD"}, "/data/www/gmf_irs": {"last_commited": "2018-12-06 20:29:50 +08:00", "oid": "99c12f2384edbd6dbbeadb143570dc17ae8fa1ed", "branch": "HEAD"}, "/data/www/xc-uds": {"last_commited": "2018-12-18 20:37:16 +08:00", "oid": "909b34bbc406115510b05ee30dfe113e6bd8fb77", "branch": "WM_branch"}, "/data/www/gmf_bms": {"last_commited": "2018-12-18 20:23:07 +08:00", "oid": "e805c6f3fef396266fb3012c7b56201ff5bc4224", "branch": "WM_branch"}, "/data/www/gmf_ipb": {"last_commited": "2018-12-06 20:29:49 +08:00", "oid": "950b44fef25a10c558c0718a11392833d659d7a7", "branch": "HEAD"}}
for x,y in c.items():
    print(x,y['branch'])