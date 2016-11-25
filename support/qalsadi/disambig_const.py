﻿#!/usr/bin/python# -*- coding=utf-8 -*-#-------------------------------------------------------------------------------# Name:        disambig_const.py# Purpose:     Arabic lexical analyser constants used for disambiguation before analysis## Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)## Created:     31-10-2011# Copyright:   (c) Taha Zerrouki 2011# Licence:     GPL#-------------------------------------------------------------------------------# import  pyarabic.araby as arabyDISAMBIGUATATION_TABLE={ # إذا كانت الكلمة الحالية "أن" تكون "أنْ" حرف نصب إذا سبقت فعلا # وتكون أنّ، من أخوات إنّ إذا كان ما بعدها اسماu'أن':{'verb':{'tag':'t','vocalized':u'أَنْ'},        'noun':{'tag':'t','vocalized':u'أَنَّ'},        'previous':{# أنّ                    u'غير': u'أَنَّ',                    u'لو': u'أَنَّ',                    u'لولا': u'أَنَّ',                    u'بما': u'أَنَّ',                    u'ربما': u'أَنَّ',                    u'لعل': u'أَنَّ',                    u'ليت': u'أَنَّ',                    u'إلا': u'أَنَّ',                    u'أم': u'أَنَّ',                    u'كما': u'أَنَّ',                    u'رغم': u'أَنَّ',                    u'بيد': u'أَنَّ',                    u'حتى': u'أَنَّ',                    u'بحجة': u'أَنَّ',                    u'ثم': u'أَنَّ',                    u'يعني': u'أَنَّ',#                   u'من': u'أَنَّ',                    u'في': u'أَنَّ',#                   u'إلى': u'أَنَّ',# أنْ                    u'هو':u'أَنْ',                    u'هي':u'أَنْ',                    u'إما':u'أَنْ',                    u'أو':u'أَنْ',                    #~ u'على':u'أَنْ',                    u'بلا':u'أَنْ',                    u'قبل':u'أَنْ',                    u'بعد':u'أَنْ',                    u'منذ':u'أَنْ',                    u'يجب':u'أَنْ',                    u'ينبغي':u'أَنْ',                    u'يمكن':u'أَنْ',                    u'يكاد':u'أَنْ',                    u'تكاد':u'أَنْ',                    u'كاد':u'أَنْ',                    u'عسى':u'أَنْ',                    u'يريد':u'أَنْ',                    u'تريد':u'أَنْ',                    u'أريد':u'أَنْ',                    u'أراد':u'أَنْ',                    u'أرادت':u'أَنْ',                    u'أوشك':u'أَنْ',                    u'أوشكت':u'أَنْ',                    u'أرادت':u'أَنْ',                    u'أرادت':u'أَنْ',                    u'أرادت':u'أَنْ',                    u'أرادت':u'أَنْ',},    },u'إن':{'verb':{'tag':'t','vocalized':u'إِنْ'},        'noun':{'tag':'t','vocalized':u'إِنَّ'},        'previous':{# أنّ                    u'والله': u'إِنَّ',                    u'ألا': u'إِنَّ',                    u'أما': u'إِنَّ',                    u'كلا': u'إِنَّ',                    u'حتى': u'إِنَّ',                    u'والله': u'إِنَّ',                    u'والله': u'إِنَّ',                    u'والله': u'إِنَّ',                    u'والله': u'إِنَّ',                    u'والله': u'إِنَّ',# أنْ                #   u'هو':u'إِنْ',                    },    }, # إذا كانت الكلمة الحالية "من" تكون "مَنْ" حرف استفهام  إذا سبقت فعلا # وتبقى ملتبسة إذا سبقت اسما. u'من':{'verb':{'tag':'t','vocalized':u'مَنْ'},         'noun':{'tag':'t','vocalized':u'ْمِن'},    },# u'ثنا':{'abbr':u'ثَنَا',}    }