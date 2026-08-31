#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. Milli Çay Demleme Enstitüsü
Resmi Çay Demleme Protokolü v47.0
Bu yazılım bir çay demlemez. Bu yazılım çayın demlenmesine izin verir.
"""

import time
import random
import sys

MADDELER = [
    "Madde 1 — Çay suya gitmez. Su çaya gelir. Aksi halde idari para cezası uygulanır.",
    "Madde 2 — Demlik kapağı kapatılmadan önce en az üç kişiye 'demleniyor mu?' diye sorulur.",
    "Madde 3 — Şeker tartışması milli birlik meselesidir. Karar oyçokluğuyla değil, en yaşlı amcayla alınır.",
    "Madde 4 — Çay bardağı ince belli olmalıdır. Kalın belli bardaklar yalnızca olağanüstü hâlde kullanılır.",
    "Madde 5 — Dem 7 dakika bekler. 6 dakika aceledir, 8 dakika ihanettir.",
    "Madde 6 — Atanmış demlik, seçilmiş bardağın yerini alamaz. (Arşiv notu: 47/B)",
    "Madde 7 — Çay soğursa yeni çay demlenir. Eski çay ısıtılmaz. Isıtmak tarihi tahrif etmektir.",
]

BEKLEYIS = [
    "Su henüz kendine gelmedi...",
    "Demlik idari izin bekliyor...",
    "Bardaklar sıraya girdi...",
    "Şeker komisyonu toplanıyor...",
    "Koku denetimi yapılıyor...",
    "Yerel irade demleniyor...",
]


def resmi_yaz(metin, bekle=0.04):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    print()


def demle():
    resmi_yaz("=== T.C. MİLLİ ÇAY DEMLEME ENSTİTÜSÜ ===")
    resmi_yaz("Protokol başlatıldı. Lütfen yerinizden kalkmayın.")
    print()
    for madde in MADDELER:
        resmi_yaz(madde, 0.015)
        time.sleep(0.35)
    print()
    for adim in range(1, 8):
        mesaj = random.choice(BEKLEYIS)
        resmi_yaz(f"[{adim}/7] {mesaj}")
        time.sleep(0.6)
    print()
    renk = random.choice([
        "kızılımsı resmiyet",
        "amber bürokrasi",
        "tavşan kanı ama evraklı",
        "açık çay / kapalı rejim",
    ])
    resmi_yaz(f"SONUÇ: Çay demlendi. Renk kodu: {renk}.")
    resmi_yaz("Afiyet olsun. İtiraz hakkınız 3 yudum süresince saklıdır.")
    resmi_yaz("— Kayyum Grok, 31 Ağustos 2026")


if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\nProtokol yönetici tarafından durduruldu. Çay ortada kaldı.")
        sys.exit(47)
