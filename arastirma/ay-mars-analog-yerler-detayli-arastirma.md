# Dünya'da Ay ve Mars'ı Andıran Yerler: Ayrıntılı Araştırma

**NASA Space Apps Challenge 2026: "Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars"**\
Hazırlanma tarihi: 14 Kasım 2026\
Temel aldığı dosya: `ay-yuzeyine-benzeyen-yerler.md` (6 yer)

> **Kaynak politikası:** Bu belgedeki tüm veri setleri ve tüm kaynaklar **yalnızca NASA'ya** aittir: nasa.gov, science.nasa.gov, NASA Earth Observatory, NASA Astrobiology, NTRS, Earthdata, JPL ve APOD. Başka takımların, başka ajansların veya NASA dışı sitelerin verisi ve bilgisi kullanılmamıştır. NASA kaynaklarında bilgisi bulunmayan konular belgede açıkça belirtilmiştir.

---

## 1. Yönetici özeti

- **NASA kaynaklarıyla doğrulanmış analog kullanımı olan yerler:**
  - Askja / İzlanda: Apollo eğitimi, Artemis II eğitimi, yeraltı buzu araştırması
  - Mauna Kea: NASA'nın yerinde kaynak kullanımı (ISRU) saha testleri
  - Atacama: NASA ARADS ve "Life in the Atacama" projeleri
- **NASA kaynaklarında yalnızca görsel ve jeolojik olarak tanımlanan yerler:**
  - Wadi Rum: NASA Earth Observatory "Ay Vadisi" ve Mars benzerliği
  - Kapadokya: NASA Earth Observatory "Ay manzarası" tanımı
  - Bardenas Reales: NASA APOD
  
  Bu üç yer için NASA'nın bir analog programı bulunamadı.
- **En önemli eksik:** Listedeki yerlerin hiçbiri NASA'nın kalıcı Ay üssü için seçtiği **Shackleton Connecting Ridge**'in iki belirleyici özelliğini birlikte taşımıyor: kutup bölgesinde olması ve hemen yanında buz barındırabilen kalıcı gölgeli bölgeler (PSR). Bu boşluğu NASA'nın kendi kutup analoğu olan **Haughton Krateri (Devon Adası)** dolduruyor (Bölüm 5).
- **Türkiye için NASA destekli güçlü bir aday var:** NASA, **Salda Gölü**'nü Mars'taki Jezero Krateri'nin analoğu olarak kullanıyor (Bölüm 6).
- **Projeye önerim:** Bu yerleri "bilinen analoglar" doğrulama seti olarak kullanalım. Puanlama modelimiz bunları üst sıralara koyuyorsa doğru çalışıyor demektir. Ardından modelin bulduğu **yeni** adayları sunalım.

---

## 2. Karşılaştırılacak hedefler ve NASA veri katmanları

### 2.1 Ay: Kalıcı üs yeri (Shackleton Connecting Ridge)
NASA, Moon Base I görevinin Ay'ın Güney Kutbu bölgesindeki Shackleton Connecting Ridge'e ineceğini açıkladı. NASA'nın tanımına göre Güney Kutbu, su ve başka bileşikler barındırabilecek soğuk ve gölgeli bölgelere sahip.

| Özellik | Ölçmek için NASA verisi |
|---|---|
| Aydınlanma ve topografya | LRO **LOLA** (kutup sayısal yükseklik modelleri) |
| Yüzey sıcaklığı ve soğuk tuzaklar | LRO **Diviner** |
| Buz ve hidrojen göstergeleri | LRO **LAMP**, **LEND**, **Mini-RF** |
| Yüzey görüntüsü ve jeoloji | LRO **LROC** (NAC, WAC) |
| Astronotun gözünden görüntüler | **Artemis II** Ay bilimi verileri (PDS, Ekim 2026) |

### 2.2 Mars: Örnek hedefler (Jezero / Gale)
| Özellik | Ölçmek için NASA verisi |
|---|---|
| Mineraller (kil, sülfat, karbonat) | MRO **CRISM** |
| Arazi | Mars Trek (**CTX** 5 m mozaiği, **MOLA**), **HiRISE** |
| Sıcaklık ve atmosfer | **THEMIS**, **MCS** |
| Yüzey iklimi ve radyasyon | MSL **REMS** ve **RAD**, Mars 2020 **MEDA** |

### 2.3 Dünya tarafı (yalnızca NASA)
| Ölçüt | NASA verisi | Not |
|---|---|---|
| Yükseklik ve eğim (60° K – 56° G arası) | **SRTMGL1 / NASADEM** (yaklaşık 30 m) | 60° kuzeyin üstünü kapsamaz |
| Kutup bölgelerinde yükseklik | **ICESat-2** (ATL14: Arktik ve Antarktika, 100 m) ve **ASTER GDEM** (NASA Terra uydusu) | Haughton (75° K) için gerekli |
| Mineraller | **EMIT** (EMITL2BMIN) | Mars'taki minerallere benzer çölleri bulmak için |
| Bitki örtüsü ve yüzey görüntüsü | **Landsat** / **HLSL30** | HLS'nin yalnızca Landsat kısmı kullanılacak |
| Sıcaklık ve kuraklık | **MERRA-2**, **MODIS** yüzey sıcaklığı (LST), **GPM IMERG** | |

> Not: NASA'ya göre Atacama gibi Dünya analoglarının hepsi Mars koşullarının yalnızca bir kısmını karşılar. Mars hem çok daha kuru hem çok daha soğuk, UV ışınımı da çok daha yoğun. Bu nedenle **bütün analoglar kısmi analogdur**.

---

## 3. Altı yerin tek tek incelenmesi

Her yer için yazılan "uygunluk" notları ekibin niteliksel değerlendirmesidir. Sayısal bir ölçüm değildir. Koordinatlar yaklaşıktır ve analiz sırasında Landsat ve SRTM ile doğrulanacaktır.

### 3.1 Kapadokya (Türkiye)
- **Konum:** Orta Anadolu (yaklaşık 38,6° K, 34,8° D)
- **NASA ne diyor:** NASA Earth Observatory, Kapadokya'yı Orta Anadolu'da yüksek ve kurak bir plato olarak tanımlıyor. Bölge zaman zaman "Ay manzarası" (moonscape) olarak anılıyor. Yıllık yağış yaklaşık 38 cm. Yumuşak volkanik tüf kolayca oyulabildiği için insanlar kayaların içine yerleşmiş, kiliseler bile oymuş. Görüntü Landsat 7 uydusunun ETM+ aletiyle çekilmiş.
- **Analog kullanımı:** NASA kaynaklarında Kapadokya için bir analog programı **bulunamadı**.
- **Ay uygunluğu:** Düşük. "Krater benzeri oyuklar" çarpma kökenli değil, aşınma kökenli. Kutup aydınlanması ve buz da yok.
- **Mars uygunluğu:** Düşük–orta. Volkanik tüf ve kuraklık var. Kayaya oyulmuş yerleşimler, radyasyondan korunan yeraltı habitatı fikri için ilham verebilir. Ancak bu fikri destekleyen bir NASA analog çalışması yok.
- **Dosyadaki düzeltme:** "Krater benzeri oyuklar" ifadesi yanıltıcı. Bunlar çarpma krateri değil.
- **Öneri:** Türkiye'den bir yer sunulacaksa NASA'nın resmi olarak kullandığı **Salda Gölü** çok daha güçlü bir aday (Bölüm 6).

### 3.2 Wadi Rum (Ürdün)
- **Konum:** Güneybatı Ürdün (yaklaşık 29,6° K, 35,4° D)
- **NASA ne diyor:**
  - Granit ve kumtaşı dağlar, kızıl kumla dolu vadilerin yanında yükseliyor. Bazı dağlar yaklaşık 1700 m yüksekliğe ulaşıyor, birçoğunun yamacı neredeyse dikey. Granitin üzerinde Kambriyen ve Ordovisiyen yaşlı kumtaşları bulunuyor. Bölge "Ay Vadisi" diye anılıyor ve 1998'de koruma altına alındı.
  - NASA Earth Observatory, Wadi Rum'un Landsat 8 görüntülerindeki renk ve dokusunun Mars'takilere çok yakın olduğunu belirtiyor. *The Martian* (2015) filminin Mars sahneleri burada çekildi.
- **Analog kullanımı:** NASA kaynaklarında bilimsel bir analog programı **bulunamadı**. NASA bölgeyi görsel bir Mars benzeri olarak tanımlıyor.
- **Dosyadaki "Ay Vadisi" adı doğru** ve NASA kaynaklarıyla destekleniyor.
- **Ay uygunluğu:** Düşük–orta. **Mars uygunluğu:** Orta–yüksek (görsel açıdan). Mineral benzerliği EMIT verisiyle sınanmalı.

### 3.3 Atacama Çölü (Şili)
- **Konum:** Kuzey Şili. NASA testleri çölün hiper-kurak çekirdeğinde yapıldı (Yungay bölgesi, yaklaşık 24° G, 70° B).
- **NASA ne diyor:**
  - Atacama, dünyanın kutup dışındaki en kurak çölü ve **eski Mars için uygun bir analog**.
  - Toprak kimyası, aşırı kuraklık ve çok düşük canlılık düzeyi nedeniyle Mars koşulları için analog olarak kullanılıyor.
  - **ARADS projesi:** NASA Astrobiyoloji Programı'nın PSTAR bileşeninden finanse ediliyor. İlk saha çalışması çölün hiper-kurak çekirdeğinde bir ay sürdü. Bölge Mars'tan çok daha sıcak olsa da kuraklığı ve toprak kimyası Mars'a dikkat çekici ölçüde benziyor. Ekip; Mars prototipi bir sondaj, örnek aktarım kolu, Signs of Life Detector (SOLID) ve 2007'de Phoenix'le uçan Wet Chemistry Laboratory'nin prototipini denedi.
  - **"Life in the Atacama":** Zoë gezgini 1 m'lik bir sondaj taşıdı.
  - **Sınırlılık:** NASA'ya göre Atacama Mars kadar kuru ve soğuk değil. Sıcaklık 0 ile 23 °C arasında değişiyor.
- **Dosyadaki düzeltme:** Dosya "Valle de la Luna" (Ay Vadisi) ile NASA test sahasını aynı yer gibi anlatıyor. NASA kaynakları testlerin **çölün hiper-kurak çekirdeğinde** yapıldığını söylüyor. Valle de la Luna için ayrı bir NASA kaynağı bulunamadı.
- **Ay uygunluğu:** Düşük–orta. **Mars uygunluğu: Yüksek.** Listedeki en güçlü Mars analoğu.

### 3.4 Askja Volkanı ve İzlanda Yaylaları
- **Konum:** Orta İzlanda (yaklaşık 65,0° K, 16,8° B)
- **NASA ne diyor:**
  - **Apollo eğitimi:** NASA'nın astronot jeoloji eğitimi kayıtlarına göre 12–16 Temmuz 1965'te bir grup astronot Orta İzlanda'da, Askja Kalderası yakınında eğitim aldı. 2–8 Temmuz 1967'deki ikinci gezide Neil Armstrong da vardı. NASA'ya göre bitki örtüsü olmayan volkanik arazi, Ay yüzeyini simüle etmek için idealdi.
  - **Artemis II eğitimi:** Artemis II mürettebatı da İzlanda'da jeoloji eğitimi aldı. NASA Artemis jeoloji eğitimi lideri Cindy Evans'a göre Apollo astronotları İzlanda'yı eğitim yerlerinin en çok Ay'a benzeyenlerinden biri olarak görüyordu. İzlanda'da Ay'a benzer volkanik süreçler, Ay'a benzer bir manzara ve Ay'daki ölçeğe yakın arazi yapıları var.
  - **Ay Güney Kutbu bağlantısı (önemli):** NASA'nın Planetary Analog Explorer sayfasına göre bilim insanları Askja yakınında **yer radarıyla gömülü buz** arıyor. Aynı teknik, gelecekte Ay Güney Kutbu yakınındaki kalıcı gölgeli bölgelerde su buzu bulmak için kullanılacak.
  - Askja çevresindeki buzul-volkanik çökeller NASA'nın Terra uydusundaki ASTER verisiyle haritalandı.
- **Ay uygunluğu:** Orta–yüksek. Volkanik jeoloji ve yeraltı buzu araştırması Ay üssü için doğrudan ilgili.
- **Mars uygunluğu:** Orta–yüksek. NASA, İzlanda'nın Vikursundar bölgesindeki kum dalgalarını Mars'taki benzerleriyle karşılaştırıyor.

### 3.5 Mauna Kea (Hawaii, ABD)
- **Konum:** Hawaii Büyük Ada (yaklaşık 19,8° K, 155,5° B)
- **NASA ne diyor:**
  - **ISRU saha testleri (2010 ve 2012):** NASA'nın ortak olduğu ve PISCES programıyla yürütülen testler. NTRS'teki rapora göre buradaki ince taneli volkanik malzeme Ay ve Mars için uygun bir analog. Kazı, saha hazırlığı ve kaynak kullanımı tekniklerinin denenmesinde kullanılıyor.
  - **2012 ISRU görevi:** NASA'nın analog görevler sayfasına göre bu testte **robotik bir Ay kutup görevi simüle edilerek su buzu ve uçucu maddeler arandı** (RESOLVE).
- **Dosyadaki düzeltme:** "Ay kraterlerini birebir simüle eden arazi" ifadesi **abartılı**. NASA kaynaklarında Mauna Kea'nın analog değeri krater biçiminden değil, **regolite benzeyen volkanik malzemeden** geliyor.
- **Ay uygunluğu: Yüksek (ISRU açısından).** Ay üssünün oksijen ve su ihtiyacıyla doğrudan ilgili.
- **Mars uygunluğu:** Orta.

### 3.6 Bardenas Reales (Navarra, İspanya)
- **Konum:** Kuzeydoğu İspanya (yaklaşık 42,2° K, 1,5° B)
- **NASA ne diyor:** NASA'nın APOD sayfası bölgedeki Castildetierra kaya oluşumunu tanıtıyor. Yapı yaklaşık 50 m yüksekliğinde, kil ve kumtaşından oluşuyor ve binlerce yıllık rüzgâr ve su aşınmasıyla şekillenmiş. Bölge doğal bir badlands (kötü arazi) alanı.
- **Analog kullanımı:** NASA kaynaklarında Bardenas Reales için bir analog programı **bulunamadı**.
- **Ay uygunluğu:** Düşük. **Mars uygunluğu:** Orta (görsel ve aşınma biçimleri). Kil içeriği EMIT verisiyle sınanabilir.

---

## 4. Toplu karşılaştırma tablosu

Puanlar ekibin niteliksel değerlendirmesidir: ●●● yüksek, ●● orta, ● düşük.

| Yer | NASA analog kullanımı | Ay (genel) | **Ay üssü (kutup + buz)** | Mars | NASA kaynaklarına göre güçlü yanı |
|---|---|---|---|---|---|
| Kapadokya | Bulunamadı | ● | ● | ●● | Kurak volkanik tüf platosu |
| Wadi Rum | Bulunamadı (görsel tanım var) | ●● | ● | ●●● (görsel) | Mars'a benzeyen renk ve doku |
| Atacama | ARADS, Life in the Atacama | ●● | ● | ●●● | Kuraklık, toprak kimyası, yaşam algılama |
| Askja / İzlanda | Apollo, Artemis II, yeraltı buzu | ●●● | ●● | ●● | Astronot eğitimi, PSR buzu aramaya benzer çalışma |
| Mauna Kea | ISRU testleri (2010, 2012) | ●●● | ●● | ●● | Regolit ve kaynak kullanımı testleri |
| Bardenas Reales | Bulunamadı | ● | ● | ●● | Aşınma biçimleri |
| **Haughton (öneri)** | HMP, 2010 Ay simülasyonu | ●●● | **●●●** | ●●● | Kutup çölü, çarpma krateri |
| **Salda Gölü (öneri)** | Perseverance / Jezero analoğu | ● | ● | **●●●** | Jezero'ya benzeyen karbonat ve delta yapıları |

---

## 5. Eksik halka: Haughton Krateri (Devon Adası, Kanada)

NASA kaynaklarına göre:

- Haughton-Mars Project, NASA'nın tanımıyla bir **görev analoğu**. Devon Adası dünyanın en büyük ıssız adası. Çorak arazisi, dondurucu sıcaklıkları ve yalıtılmışlığı Mars'a ve diğer gezegen hedeflerine benziyor.
- **Ay üssü bağlantısı:** NASA'nın 2011 tarihli teknik raporuna (NASA/TM-2011-216157) göre araştırma istasyonu Haughton Krateri'nin kenarında kurulu. Bu, Ay'da Shackleton Krateri'nde kurulacak bir üssün konumuna çok benziyor. İstasyon, birkaç bin kilometrekarelik alandaki tek altyapı.
- **2010 simülasyonu:** NASA, Haughton'da Ay'ın Güney Kutbu'ndaki **Shackleton Krateri'nden Malapert Dağı'na** uzanan yaklaşık 120 km'lik (75 mil) bir robotik konvoyu simüle etti.
- **Yaş düzeltmesi:** NTRS'teki çalışmaya göre Haughton'un yaşı yaklaşık **38 milyon yıl** (Eosen). Daha önceki tahminler Miyosen yaşını gösteriyordu.
- **Konum:** yaklaşık 75° K, 90° B. SRTM bu enlemi kapsamıyor, bu yüzden **ICESat-2** ve **ASTER GDEM** kullanılmalı.

---

## 6. Türkiye için NASA destekli aday: Salda Gölü (Burdur)

- NASA'ya göre Salda Gölü, Jezero Krateri'ndekilere benzeyen karbonat mineralleri ve delta çökelleri barındıran, **dünyada bilinen tek göl**.
- Kıyıdaki beyaz kumlar **hidromagnezit** içeriyor. Bu mineral Jezero'da saptanan karbonatlara benziyor. Bu çökellerin, mikropların yardımıyla oluşan **mikrobiyalit** tepeciklerinden aşındığı düşünülüyor.
- NASA'nın Mars 2020 ekibi 2019'da göle saha çalışması yaptı. Jezero görüntüsü MRO'nun CTX kamerasından, Salda görüntüsü Landsat 8'den alındı.
- **Projede kullanımı:** Mars hedefi Jezero seçilirse Salda Gölü, Türkiye'den sunulabilecek NASA kaynaklı en güçlü doğrulama noktası.

---

## 7. Projede kullanım önerisi (yalnızca NASA verisi)

1. **Doğrulama seti:**
   - Pozitif örnekler: Atacama, Askja, Mauna Kea, Haughton, Salda.
   - Negatif kontroller: bitki örtüsü yoğun alanlar (Landsat NDVI yüksek olan yerler).
   - Model pozitifleri üst sıralara koyuyorsa çalışıyor demektir.
2. **Mars puanı:** kuraklık (MERRA-2, GPM), mineral (EMIT ve CRISM karşılaştırması), arazi (SRTM/NASADEM ve MOLA karşılaştırması), bitki yokluğu (Landsat NDVI).
3. **Ay üssü puanı:** enlem ve aydınlanma, yüzey sıcaklığı (MODIS LST, MERRA-2), kalıcı donmuş zemin, sırt ve krater topografyası (kutuplarda ICESat-2 ve ASTER GDEM). Karşılaştırma için LOLA ve Diviner kullanılacak.
4. **Görev türüne göre ağırlıklandırma:** ISRU testi (Mauna Kea benzerleri), yeraltı buzu arama (Askja benzerleri), yaşam algılama (Atacama ve Salda benzerleri), üs operasyonları (Haughton benzerleri).
5. **Yeni NASA verisi:** Artemis II mürettebatının çektiği görüntüler (PDS, Ekim 2026) Ay tarafında görsel karşılaştırma katmanı olarak kullanılabilir.

---

## 8. Kaynaklar (yalnızca NASA)

**Ay üssü ve yeni veriler**
- NASA, Moon Base güncellemesi (Mayıs 2026): https://nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions
- NASA, Artemis III iniş bölgeleri: https://www.nasa.gov/news-release/nasa-provides-update-on-artemis-iii-moon-landing-regions/
- NASA, Artemis II Ay bilimi verileri (Ekim 2026): https://www.nasa.gov/blogs/missions/2026/10/07/nasa-releases-artemis-ii-lunar-science-data-images/

**Analoglar genel**
- NASA, 10 Things to Know About Planetary Analogs: https://science.nasa.gov/solar-system/planetary-analogs/10-things-to-know-about-planetary-analogs/
- NASA, Planetary Analog Explorer: https://science.nasa.gov/solar-system/analog-explorer/

**Kapadokya**
- NASA Earth Observatory, Göreme National Park: https://earthobservatory.nasa.gov/images/38876/goreme-national-park-turkey

**Wadi Rum**
- NASA Earth Observatory, Movie Mars on Earth: https://science.nasa.gov/earth/earth-observatory/movie-mars-on-earth-148764/
- NASA Earth Observatory, Wadi Rum (2001): https://science.nasa.gov/earth/earth-observatory/wadi-rum-jordan-49945/

**Atacama**
- NASA Astrobiology, ARADS: https://astrobiology.nasa.gov/news/nasa-tests-life-detection-drill-in-the-atacama-desert/
- NASA, Tire Tracks on "Mars": https://www.nasa.gov/image-article/tire-tracks-mars-atacama-rover-astrobiology-drilling-studies/
- NASA Astrobiology, Field Sites: https://astrobiology.nasa.gov/research-locations/
- NASA Astrobiology, The Driest Place on Earth: https://astrobiology.nasa.gov/nai/articles/2002/4/24/the-driest-place-on-earth/index.html
- NASA, Life in the Atacama (Zoë): https://www.nasa.gov/general/drilling-our-way-to-life-on-mars-rover-mounted-drill-autonomously-explores-subsurface-life-in-the-atacama-desert-chile/

**Askja / İzlanda**
- NASA, Astronot Jeoloji Eğitimi kayıtları (ALSJ): https://www.nasa.gov/wp-content/uploads/static/history/alsj/AstronautGeologyTraining.pdf
- NASA, Apollo 13 European Goodwill Tour: https://www.nasa.gov/history/50-years-ago-apollo-13-aquarius-european-goodwill-tour/
- NASA, Artemis II Crew Uses Iceland Terrain: https://science.nasa.gov/missions/artemis/nasas-artemis-ii-crew-uses-iceland-terrain-for-lunar-training/
- NASA ESPO, Askja ASTER haritalaması: https://espo.nasa.gov/atom/content/Remote_sensing_and_geologic_mapping_of_glaciovolcanic_deposits_in_the_region_surrounding

**Mauna Kea**
- NTRS, ISRU Field Tests 2010 and 2012 at Mauna Kea: https://ntrs.nasa.gov/citations/20140008708
- NASA analog missions, ISRU 2012 (arşivlenmiş nasa.gov sayfası): https://webarchive.library.unt.edu/web/20130221205815/http://www.nasa.gov/exploration/analogs/isru/index.html

**Bardenas Reales**
- NASA APOD, Milky Way Over Spain's Bardenas Reales: https://science.nasa.gov/image-article/apod-2013-september-2-milky-way-over-spains-bardenas-reales/

**Haughton**
- NASA/TM-2011-216157: https://ntrs.nasa.gov/api/citations/20110011887/downloads/20110011887.pdf
- NASA Analogs blog, HMP-2010: https://blogs.nasa.gov/analogsfieldtesting/2010/08/03/post_1280841076434/
- NTRS, Mars Always Cold, Sometimes Wet (Haughton yaşı): https://ntrs.nasa.gov/citations/20050170975

**Salda Gölü**
- NASA Earth Observatory, Jez like Mars: https://science.nasa.gov/earth/earth-observatory/jez-like-mars-147041/
- NASA Earth Matters, What a Lake in Turkey Can Tell Us about Mars: https://science.nasa.gov/blogs/earth-matters/2021/02/17/what-a-lake-in-turkey-can-tell-us-about-mars/

**Veri setleri**
- ICESat-2 ATL14 (NASA NSIDC DAAC): https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-atl14-005
- SRTMGL1 (NASA LP DAAC): https://www.earthdata.nasa.gov/data/catalog/lpcloud-srtmgl1-003
- HLSL30 (NASA LP DAAC): https://www.earthdata.nasa.gov/data/catalog/lpcloud-hlsl30-2.0
- EMIT L2B Mineral (NASA LP DAAC): https://cmr.earthdata.nasa.gov/search/concepts/C2408034484-LPCLOUD.html
- NASA Solar System Treks (Moon Trek / Mars Trek): https://trek.nasa.gov
