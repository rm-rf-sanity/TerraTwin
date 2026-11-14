# Yetkili NASA ürünleri: işlem kuralları

14 Kasım2026 denetimi. Güncel koleksiyon kimlikleri ve makineye okunabilir kurallar `data/protected-source-registry.json` içindedir. Bir koleksiyonun katalogda bulunması, belirli alandaki piksel kalitesinin yeterli olduğunu göstermez. Gözlem ve işleme sürümü ayrı kaydedilmelidir.

## MOD13Q1.061 — NDVI

250m,16günlük,HDF4,sinusoidal ürün. NDVI ham aralığı−2000…10000;dolgu−3000; fiziksel değer ham×0.0001. HDF `scale_factor=10000` varsa bu bölen konvansiyonudur; otomatik çarpılmaz. `250m 16 days pixel reliability`:−1eksik,0iyi,1marjinal,2kar/buz,3bulut. Muhafazakâr başlangıç0; ayrıntılıQA alt2bit0, bit8/10/14/15 kapalı, yüksek aerosol dışarıda, kara bayrağı1. Marjinal1 ancak ayrı ve açık kuralla kullanılabilir. AOI konumu dosyanın HDF-EOS projeksiyon/köşe metaverisinden bulunmalı; h/v tile koordinatı enlem-boylam değildir. NDVI bitki alanı oranı değildir. [NASA dosya tanımı](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD13Q1), [NASA C6.1 kılavuzu](https://modis-land.gsfc.nasa.gov/pdf/MOD13_User_Guide_V61.pdf).

## VNP46A2.2 — Gece ışıkları

V2dosya tanımı2.0.4,15yay-saniyesi,2400²enlem-boylam ızgarası. `DNB_BRDF-Corrected_NTL` Float;dolgu−999.9;geçerli≥0;nW·cm⁻²·sr⁻¹. V1’in0.1çarpanı V2radyansına uygulanmaz; gerçek dosya öznitelikleri doğrulanır. `Mandatory_Quality_Flag=0` yüksek kalite;1–5düşük kalite. `QF_Cloud_Mask`:gecebit0=0, kalitebits4–5=3, bulutbits6–7=0; gölge8,sirrus9,kar/buz10,aurora12,tutulma13sıfır. Bunlar muhafazakâr pilot filtresidir. Gap-filled ve doğrudan gözlenen radyans ayrılmalı; `Latest_High_Quality_Retrieval` gün yaşını belirtir. [NASA V2dosya tanımı](https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/2/VNP46A2_v2.0.fs), [NASA ürün sayfası](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/VNP46A2).

## EMITL2BMIN.002 — Mineraller

CMR’de001ve002var;002yeniden işleme Ekim2026’da başladı ve arşiv tamamlanmış sayılmamalı. V1’e sessiz dönüş yapılmamalı. [NASA sürüm duyurusu](https://forum.earthdata.nasa.gov/viewtopic.php?t=8322).

NASA referans düzeni kökte iki mineralID/band-depth grubu, `mineral_metadata` ve `location` içerir. ID0eşleşme yoktur;−9999dolgu ayrı tutulur. MINUNCERT eş-zaman/orbit/sahne dosyası ve L2A_MASK gerekir; V2gerçek şeması okunmalıdır. Mineral türü ve bant derinliği, kütle bolluğu veya Mars eşleşmesi değildir. [NASA mineral öğreticisi](https://nasa.github.io/LPDAAC-Data-Resources/external/Working_with_EMIT_L2B_Mineralogy.html).

GLTkoordinatları1tabanlıdır;GLT0geçersiz; NumPy yerleştirmesi `raw[glt_y-1,glt_x-1]`. Ortorektifiye grid piksel merkezleri geotransformdan hesaplanır. L2A_MASK band adları okunmalı; eski band sıraları körlemesine kullanılmamalı. [NASA uygulaması](https://raw.githubusercontent.com/nasa/EMIT-Data-Resources/main/python/modules/emit_tools.py).

## ASTGTM.003 — Güncel ürün sürümüne geçiş

DEM:3601²,1yay-saniyesi,Int16,1m/DN,−9999eksik;0deniz seviyesi için geçerli. YatayWGS84,düşeyEGM96. NUM, basit sahne sayacı değildir:0–50V3,60–110V2,131–184PRISM,201–223SRTM;231–246çeşitli dolgu kaynakları,250enterpolasyon. Tam kod tablosuJSON’da. Kaynak sınıfı ve sayısı ayrı raporlanmalı; `NUM>=3` tek başına genel kalite testi değildir. [NASA V3kılavuzu](https://www.earthdata.nasa.gov/s3fs-public/2025-04/ASTGTM_User_Guide_V3.pdf).

Salda için gerçek `ASTGTMV003_N37E029_dem.tif` ve `_num.tif` bulundu(~24.31MB toplam). NASADEM001aynı tile alternatifi~12.18MB. Resmî indirme URL’leriJSON’da; dosyaların indirilmesi bu kaynak incelemesinin parçası değildir. Bu yeni ürün sürümü, tarihsel2000–2013gözlemleri2026ölçümüne dönüştürmez. [NASA arşiv açıklaması](https://data.nasa.gov/dataset/aster-global-digital-elevation-model-netcdf-v003-90e58).
