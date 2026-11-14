# Dünya'da Kalıcı Ay Üssü ve Mars Analogları: Birleşik Araştırma Raporu

**NASA Space Apps Challenge 2026**\
**Görev:** "Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars"\
**Hazırlanma tarihi:** 14 Kasım 2026\
**Hazırlayan:** Dr. Şebnem Çelik ve ekibi için derlenmiştir

> **Kaynak politikası:** Bu rapordaki bütün veri setleri ve bütün kaynaklar **yalnızca NASA'ya** aittir: nasa.gov, science.nasa.gov, NASA Earth Observatory, NASA Astrobiology, NASA Technical Reports Server (NTRS), NASA Earthdata, NASA Jet Propulsion Laboratory (JPL), NASA Space Science Data Coordinated Archive (NSSDCA) ve NASA'nın Astronomy Picture of the Day (APOD) sayfaları. Başka takımların çalışmaları, başka uzay ajanslarının veri setleri veya NASA dışı siteler kaynak olarak kullanılmamıştır. Bir konu hakkında NASA kaynaklarında bilgi bulunamadığında bu durum metinde açıkça yazılmıştır.

> **Bu rapor neyi birleştiriyor:** Bu belge, bu çalışma sürecinde üretilen bütün içerikleri tek çatı altında toplar:
> 1. Görevin ilk araştırması ve NASA'nın yeni açıkladığı verilerin özeti,
> 2. Ekibin hazırladığı `ay-yuzeyine-benzeyen-yerler.md` dosyasındaki altı yer,
> 3. Bu altı yerin ayrıntılı incelemesi ve düzeltmeleri (md ve Word sürümleri),
> 4. Yalnızca NASA verisine dayanacak şekilde yapılan güncelleme,
> 5. Yeni eklenen NASA kaynakları: Moon Base aşamaları, LRO aletleri, insanlı Mars iniş ölçütleri, EMIT ve kutup yükseklik verileri.

---

## İçindekiler

1. Yönetici özeti
2. Görevin tanımı ve bu raporun amacı
3. NASA Moon Base programı: neyi taklit etmeye çalışıyoruz?
4. Ay Güney Kutbu'nun ortamı ve LRO verileri
5. Yeni açıklanan NASA verileri
6. Mars tarafı: hedefler ve insanlı iniş ölçütleri
7. Analog kavramı: NASA'nın tanımı ve sınırları
8. Başlangıç noktası: ekibin altı yer listesi
9. Altı yerin ayrıntılı incelemesi
10. NASA'nın kullandığı ek analoglar
11. Toplu karşılaştırma
12. Dünya tarafındaki NASA veri katmanları
13. Yöntem: puanlama modeli
14. Doğrulama planı
15. Uygulama ve yazılım mimarisi
16. Hackathon zaman planı
17. Sunum ve anlatı stratejisi
18. Riskler, sınırlılıklar ve açık sorular
19. Önceki sürümlerde yapılan düzeltmeler
20. Sözlük
21. Kaynaklar (yalnızca NASA)
22. Ekler: örnek aday kartı, örnek proje özeti, veri kontrol listesi, iş bölümü, jüri soruları ve cevapları

---

## 1. Yönetici özeti

Bu raporun temel bulgusu şu: Görev, Ay'da üs yeri seçmemizi istemiyor. İstenen şey, **Dünya'da**, NASA'nın kalıcı Ay üssü için seçtiği yere ve Mars'taki hedef bölgelere benzeyen **yeni yerleri bulmak ve bu yerleri verilerle tarif etmek**. Bu ayrım projenin her adımını belirliyor. Bizim ürünümüz Ay'a dair bir harita değil, Dünya'ya dair bir benzerlik haritası olacak. Ay ve Mars verileri ise bu haritanın "hedef profillerini" tanımlamak için kullanılacak.

Raporun ana sonuçları şunlar:

**Birinci sonuç: Ay üssünün yeri artık belli.** NASA, Mart 2026'daki "Ignition" etkinliğinde Moon Base programını duyurdu. Mayıs 2026'da ilk robotik görev olan Moon Base I'in Ay'ın Güney Kutbu'ndaki **Shackleton Connecting Ridge** bölgesine ineceğini açıkladı. Bu, eski analog çalışmalarının çoğunun dayandığı Artemis III iniş bölgesi listelerinden daha somut bir hedef. Projemiz bu güncel hedefi esas alırsa hem en yeni NASA kararlarına dayanmış olur hem de eski listelere dayanan çalışmalardan ayrışır.

**İkinci sonuç: Ekibin altı yerlik listesi değerli ama eksik.** Listedeki Kapadokya, Wadi Rum, Atacama, Askja, Mauna Kea ve Bardenas Reales gerçekten Ay'ı veya Mars'ı andıran yerler. Bunlardan üçünün NASA kaynaklarıyla belgelenmiş bir analog kullanımı var:

- Askja ve İzlanda: Apollo ve Artemis II astronot eğitimi, ayrıca yeraltı buzu araştırması
- Mauna Kea: yerinde kaynak kullanımı (ISRU) saha testleri
- Atacama: Mars yaşam algılama ve sondaj testleri

Diğer üçü (Wadi Rum, Kapadokya, Bardenas Reales) NASA kaynaklarında yalnızca görsel veya jeolojik açıdan tanımlanıyor. NASA'nın bu üç yer için bir analog programı bulunamadı.

**Üçüncü sonuç: Listede kutup analoğu yok.** Shackleton Connecting Ridge'in en önemli iki özelliği, kutup bölgesinde olması ve hemen yanında buz barındırabilen kalıcı gölgeli bölgelerin (PSR) bulunması. Altı yerin hiçbiri bu iki özelliği birlikte taşımıyor. NASA'nın bu boşluğu dolduran kendi analoğu **Haughton Krateri (Devon Adası, Kanada)**. NASA'nın 2011 tarihli teknik raporuna göre Haughton'daki araştırma istasyonu krater kenarında kurulu ve bu konum, Shackleton Krateri'nde kurulacak bir Ay üssünün konumuna çok benziyor. NASA 2010'da Haughton'da, Shackleton Krateri'nden Malapert Dağı'na uzanan bir robotik konvoyu da simüle etti.

**Dördüncü sonuç: Türkiye'den NASA'nın resmi olarak kullandığı bir analog var.** NASA, Burdur'daki **Salda Gölü**'nü Perseverance gezgininin incelediği Jezero Krateri'nin analoğu olarak kullanıyor. NASA'ya göre Salda, Jezero'dakilere benzeyen karbonat mineralleri ve delta yapıları barındıran, dünyada bilinen tek göl. Türkiye'den bir yer sunmak istiyorsak Kapadokya yerine Salda çok daha güçlü bir aday.

**Beşinci sonuç: Bütün analizi yalnızca NASA verisiyle yapmak mümkün.** Ay tarafında LRO'nun aletleri (LOLA, Diviner, LAMP, LEND, Mini-RF, LROC) ve Artemis II verileri var. Mars tarafında MRO (CRISM, CTX, HiRISE), Mars Odyssey (THEMIS), MGS (MOLA) ve gezgin verileri var. Dünya tarafında SRTM/NASADEM, ICESat-2, ASTER GDEM, Landsat, EMIT, MERRA-2, MODIS ve GPM var. Tek dikkat edilmesi gereken nokta şu: SRTM 60° kuzeyin üstünü kapsamadığı için kutup analogları (örneğin 75° kuzeydeki Haughton) için ICESat-2 ve ASTER GDEM kullanılmalı.

**Önerilen proje:** Ay üssü ve Mars için iki ayrı "hedef profil" tanımlayıp Dünya'nın karalarını bu profillere göre puanlayan, puanın her bileşenini hangi NASA verisinden geldiğiyle birlikte gösteren bir benzerlik haritası. Modelin doğruluğu, NASA'nın zaten kullandığı analogların (Atacama, Askja, Mauna Kea, Haughton, Salda) üst sıralarda çıkıp çıkmadığına bakılarak ölçülecek. Asıl katkı ise modelin önerdiği **yeni** adaylar olacak.

---

## 2. Görevin tanımı ve bu raporun amacı

### 2.1 Görevin özü

NASA Space Apps Challenge 2026'nın bu görevi, Ay'a ve Mars'a yapılacak görevlerin Dünya'da prova edilmesiyle ilgili. Görev metnine göre gelecekteki iniş yerlerinin ve Ay üssü konumlarının seçimi; topografya, jeoloji, çevre koşulları ve kaynaklar gibi pek çok etkene bağlı. Dünya'da Ay'a veya Mars'a benzeyen yerler, görev ekiplerinin ekipmanlarını ve yöntemlerini uçuştan önce denemesine imkân veriyor. Ancak görev metni bu yerlerin henüz iyi tanımlanmadığını vurguluyor. Katılımcılardan, NASA'nın açık Dünya, Ay ve Mars verilerini kullanarak yeni Dünya analoglarını bulmaları ve tanımlamaları isteniyor. Aday ortamlar arasında çöller, kutup bölgeleri, volkanik ve kurak araziler ile mağaralar sayılıyor.

Görev başlığındaki "Permanent Moon Base Locations" ifadesi önemli. Görev, genel olarak "Ay'a benzeyen yerler" değil, **kalıcı Ay üssünün kurulacağı yerlere** benzeyen yerler istiyor. NASA'nın 2026 boyunca açıkladığı Moon Base programı bu yeri somutlaştırdığı için hedefimiz artık belirsiz değil (Bölüm 3).

### 2.2 Görev metninden çıkan gereksinimler

Görev metnini, projede karşılanması gereken somut gereksinimlere şöyle çevirebiliriz:

1. **Hedef tanımı:** En az bir Ay üssü konumu ve en az bir Mars konumu açıkça tanımlanmalı.
2. **Ölçülebilir ölçütler:** Hedeflerin özellikleri (topografya, jeoloji, çevre, kaynaklar) ölçülebilir değişkenlere çevrilmeli.
3. **Açık veri kullanımı:** Ölçütler NASA'nın açık verileriyle hesaplanmalı.
4. **Yeni adaylar:** Çıktı yalnızca bilinen analogları listelememeli, yeni aday yerler önermeli.
5. **Tanımlama (karakterizasyon):** Her aday için neden benzer olduğu, hangi bakımdan farklı olduğu ve hangi tür testler için uygun olduğu açıklanmalı.
6. **Kısmi analog bilinci:** Hiçbir yerin hedefi birebir kopyalamadığı kabul edilmeli. Benzerlik, hangi açıdan benzediği belirtilerek sunulmalı.

### 2.3 Bu raporun amacı

Bu rapor, yukarıdaki gereksinimleri karşılayacak bir projenin bilimsel ve teknik temelini oluşturmak için hazırlandı. Rapor üç işlev görüyor:

- **Arka plan:** Ekip üyelerinin Moon Base programını, Ay Güney Kutbu'nun ortamını, Mars hedeflerini ve analog kavramını aynı seviyede anlaması için.
- **Kanıt tabanı:** Ekibin listesindeki yerlerin hangilerinin NASA tarafından gerçekten analog olarak kullanıldığını, hangilerinin yalnızca görsel benzerlik taşıdığını ayırmak için.
- **Uygulama planı:** Veri katmanlarını, puanlama yöntemini, doğrulama planını ve hackathon süresince yapılacak işleri tanımlamak için.

### 2.4 Bu raporun ne olmadığı

Bu rapor projenin kendisi değil. Jürinin göreceği şey, bu plana göre kurulacak analiz ve harita olacak. Rapordaki uygunluk notları (●●● gibi işaretler) ekibin niteliksel değerlendirmesidir, veriyle hesaplanmış skorlar değildir. Model kurulduğunda bu notların yerini gerçek skorlar alacak.

---

## 3. NASA Moon Base programı: neyi taklit etmeye çalışıyoruz?

### 3.1 Programın doğuşu

NASA, Moon Base'i "insanlığın ilk Ay karakolu" olarak tanımlıyor. Burası, astronotların Ay'ın Güney Kutbu yakınında yaşayıp çalışacağı ve keşif yapacağı bir yer olacak. Program 24 Mart 2026'da NASA'nın "Ignition" etkinliğinde duyuruldu. Bu etkinlikte NASA, Ay'da üs kurmak ve kalıcı insan varlığı sağlamak için aşamalı bir yaklaşım tanıttı.

Programın 2026 içindeki kilometre taşları NASA'nın Moon Base sayfasında şöyle sıralanıyor:

- **24 Mart:** Ignition etkinliği ve programın duyurulması
- **26 Mayıs:** İlk Moon Base görevleri, gezgin sözleşmeleri ve iniş aracı görevlerinin açıklanması
- **30 Haziran:** Ek bilimsel görevlerin ve yeni fırsatların duyurulması
- **24 Temmuz:** CAPSTONE 02 görevinin duyurulması
- **Ağustos:** İlk dört ticari iniş aracını tanıtan üçüncü Moon Base güncellemesi
- **Ekim:** Robotik gezginler ve Ay arazi araçları (LTV) üzerine güncelleme
- **7 Kasım:** Kennedy Uzay Merkezi'ndeki MAX POWER etkinliğinde yeni ödüller ve görev güncellemeleri

### 3.2 Konum: Güney Kutbu ve Shackleton Connecting Ridge

NASA'nın aşamalar sayfasına göre Moon Base bölgesi, Ay'ın Güney Kutbu ve su buzu barındırabilecek kalıcı gölgeli kraterleri kapsıyor. Adı geçen belirli konumlar şunlar:

- **Shackleton Connecting Ridge:** Blue Moon MK1 aracının iniş denemesi yapacağı yer.
- **Reiner Gamma:** Güçlü manyetik anomalisi olan bir "Ay girdabı" (lunar swirl). Burası kutupta değil; IM-3 görevinin hedefi.
- **Ay'ın uzak yüzü:** Blue Ghost Mission 2'nin hedefi.
- **Olası Artemis iniş yerleri:** MoonFall görevi bunları haritalayacak.

Mayıs 2026 duyurusuna göre **Moon Base I**, Blue Origin'in Blue Moon Mark 1 aracıyla en erken 2026 sonbaharında fırlatılacak ve Shackleton Connecting Ridge'e inecek. Görev, roket egzozunun yüzeye etkisini inceleyen aletler ve bir lazer reflektörü taşıyacak. Bu nedenle bizim "Ay üssü hedef profilimiz", Shackleton Connecting Ridge ve çevresinin özelliklerinden türetilecek.

### 3.3 Birinci aşama (şimdi – 2029): Erişim, deney, öğrenme

NASA bu aşamada astronotlar gelmeden önce iniş, hareketlilik, iletişim ve kaynak teknolojilerini robotik görevlerle test edecek.

**İniş araçları ve teslimatlar:**
- **Blue Origin Blue Moon MK1 "Endurance":** Hassas iniş, otonom yönlendirme ve navigasyon ile kriyojenik itki gösterimi yapacak. Langley Araştırma Merkezi'nin roket egzozunun yüzeye etkisini inceleyen SCALPSS aletini ve Goddard'ın Lazer Reflektör Dizisi'ni taşıyacak.
- **Voyager Technologies Griffin-1:** 2026 sonunda fırlatılması planlanıyor. Johnson'ın LDES toz sensörünü, Marshall'ın Ay LiDAR haritalama gösterimini, Goddard'ın iki lazer reflektör dizisini ve regolitteki helyum-3'ü ölçecek METAL aletini taşıyacak.
- **Intuitive Machines IM-3 (Nova-C "Trinity"):** Ay girdaplarını inceleyecek Lunar Vertex'i ve LDES'i taşıyacak. Ayrıca planlanan Ay veri ağının ilk aktarım uydusu olan Altus-1'i yörüngeye bırakacak.
- **Firefly Blue Ghost Mission 2:** Ay'ın uzak yüzüne inecek. NASA'ya göre bu, Amerika'nın uzak yüze ilk inişi olacak.

**Gezginler ve hareketlilik:**
- **VIPER:** 2027 sonunda ikinci Blue Moon MK1 ile Güney Kutbu'na ulaşacak. 1 m'lik bir matkabı var. Kalıcı gölgeli kraterlerdeki su buzunu ve diğer uçucu maddeleri haritalayacak. NASA bunu "başka bir dünyanın ilk kaynak haritası" olarak tanımlıyor.
- **PROMISE (JPL):** Altı tekerlekli, nükleer enerjili bir gezgin (ayrıntılar Bölüm 3.6'da).
- **MoonFall (JPL):** 2028'de ulaşacak dört itici motorlu dron. Her biri bir Ay günü içinde birden fazla uçuş yaparak yüksek çözünürlüklü arazi haritaları çıkaracak, radyasyonu ölçecek, yeraltı buzu arayacak ve konum verisi sağlayacak.
- **Ay arazi araçları (LTV, 2028):** NASA Astrolab'ın CLV-1 aracını ve Lunar Outpost'un Pegasus aracını seçti. Bunlar basınçsız araçlar. İki astronot ve yük taşıyabiliyor; otonom, uzaktan kumandalı veya tek astronotla kullanılabiliyor.

**Navigasyon ve iletişim:**
- **CAPSTONE 02 (2027):** Ay yörüngesinde iki küçük uzay aracı buluşma, yakın operasyon, otonom navigasyon ve Ay–Dünya arası iletişim testleri yapacak. Görev ayrıca radyasyon ortamını da ölçecek.

### 3.4 İkinci aşama (2029 – 2032): İnşa et ve genişlet

NASA bu aşamada ilk uzun vadeli altyapıyı kuracak ve bunu birden fazla konuma yaymayı hedefliyor. Öncelikler arasında erken dönem enerji sistemleri, yük taşıma, lojistik ve iletişim sayılıyor. Japonya'nın geliştirdiği basınçlı gezginin de bu aşamada kullanılması bekleniyor. NASA'ya göre bu araç mobil bir yaşam alanı ve laboratuvar olacak. Astronotlar içinde uzay giysisi olmadan çalışabilecek. Görevler 28 güne kadar sürebilecek ve yük ikmali 14 güne kadar aralıklarla yapılabilecek.

NASA'nın aşamalar sayfası bu aşamanın enerji donanımı hakkında ayrıntı vermiyor.

### 3.5 Üçüncü aşama (2032 ve sonrası): Yaşa ve çalış

NASA bu aşamada Güney Kutbu yakınında, astronotların uzun süre kalabileceği kalıcı bir karakol kuracak. Yaşam alanları, enerji sistemleri, iletişim ve ulaşım temel bileşenler olarak sayılıyor. Karakol hem daha kapsamlı bilimsel çalışmaları destekleyecek hem de daha uzak uzay görevlerine hazırlık yapılmasını sağlayacak. NASA'nın sayfası bu bileşenlerin tasarımı hakkında ayrıntı vermiyor ve plan geliştikçe yeni görevlerin ekleneceğini belirtiyor.

### 3.6 7 Kasım 2026 duyuruları

NASA'nın 7 Kasım 2026'daki Moon Base güncellemesi bu rapor için özellikle önemli. Çünkü yarışmadan yalnızca bir hafta önce açıklandı ve projeye "en güncel NASA kararları" boyutunu katıyor.

**PROMISE gezgini:** NASA, PROMISE (Polar Rover for Observation, Mapping, and In-Situ Exploration) gezgininin geliştirilmesine devam etme kararı aldı. Altı tekerlekli gezgin Ay'ın Güney Kutbu'na inecek. Görevleri şunlar:

- yüzeyi ve yeraltını tanımlamak,
- kaynak potansiyelini değerlendirmek,
- iniş yeri seçimi ve gelecekteki altyapı için veri sağlamak.

Gezgini JPL yönetecek. JPL, gezgini Curiosity ve Perseverance Mars gezginlerinin yedek uçuş parçaları ve mühendislik test modelleriyle inşa edecek. Gezgin şu donanımı taşıyacak:

- yaklaşık 1 m derinlikten regolit çıkarıp buz ve diğer kaynakları inceleyecek bir matkap,
- yüzey malzemesinin kimyasal bileşimini analiz edecek spektrometreler,
- sıcaklık ve radyasyon sensörleri ile görünür ışık kameraları.

NASA'ya göre nükleer enerjili gezgin, uzun Ay gecelerinde ve buz barındırdığı düşünülen kalıcı gölgeli bölgelerde çalışabilecek. Fırlatma 2028 sonu için hedefleniyor ve görev 18 ay sürecek.

**Yüzey enerji altyapısı:** NASA, miniCAST (Mini-Communications and Solar Tower) adlı küçük bir iletişim ve güneş kulesi için ticari bileşenler satın alacak. Bunlar güneş panelleri, bataryalar ve kablosuz enerji aktarım donanımı. Bu duyuru, Ay üssünün güneş enerjisine ne kadar bağlı olduğunu gösteriyor. Bu bağımlılık da bizim "aydınlanma" ölçütümüzün neden kritik olduğunu açıklıyor.

**Diğer duyurular:** NASA ayrıca CLPS'nin bir sonraki aşaması için sekiz şirket seçti, fırlatma ve uzayda taşıma kapasitesini geliştirmek için altı görev siparişi verdi ve Ay–Dünya arası bir iletişim gösterimi için SpaceX'i seçti.

### 3.7 Bu programdan proje için çıkan sonuçlar

Moon Base programının ayrıntıları, Dünya'daki analoglarda hangi özellikleri aramamız gerektiğini doğrudan belirliyor:

| Moon Base ihtiyacı | NASA'daki karşılığı | Dünya analoğunda aranacak özellik |
|---|---|---|
| Güneş enerjisi | miniCAST güneş kulesi | Uzun süreli, ufka yakın açılı güneş ışığı; yüksek enlem |
| Su buzu ve kaynak | VIPER, PROMISE, MoonFall | Kalıcı donmuş zemin, gömülü buz, soğuk tuzak benzeri gölgeli alanlar |
| Hassas iniş | Blue Moon MK1, SCALPSS | Düz sırtlar, düşük eğimli iniş alanları |
| Arazi araçları | LTV, basınçlı gezgin | Kayalık, engebeli, bitkisiz arazi; krater kenarı ve sırt topoğrafyası |
| İletişim ve navigasyon | Altus-1, CAPSTONE 02 | Yalıtılmış, altyapısız, iletişimi zor bölgeler |
| Yalıtılmışlık ve lojistik | Kalıcı karakol | Ulaşımı zor, insan yerleşiminden uzak bölgeler |

Bu tablo, Bölüm 13'teki puanlama modelinin ölçütlerinin neden seçildiğini de açıklıyor.

---

## 4. Ay Güney Kutbu'nun ortamı ve LRO verileri

### 4.1 Neden Güney Kutbu?

NASA, Artemis III iniş bölgeleriyle ilgili açıklamasında Güney Kutbu'nu Ay'ın en eski arazilerine erişim sunan, su ve başka bileşikler barındırabilecek soğuk ve gölgeli bölgelere sahip bir yer olarak tanımlıyor. NASA'nın Artemis lunar bilim lideri Sarah Noble'a göre Güney Kutbu, Apollo görevlerinin indiği yerlerden tamamen farklı bir ortam.

Güney Kutbu'nun özel olmasının nedeni Ay'ın dönme ekseninin yörünge düzlemine göre çok az eğik olması. NASA'nın LAMP aletine ait teknik özetine göre Ay'ın eksen eğikliği düşük olduğu için yüksek enlemlerdeki çukurlarda kalıcı gölgeler oluşuyor. Bu gölgelerdeki sıcaklıklar, uçucu maddeleri Ay'ın yaşı boyunca tutabilecek kadar düşük. Aynı belge, kutuplarda aydınlanmanın günlük, mevsimsel ve 18 yıllık bir döngüyle değiştiğini de belirtiyor.

Bu durum Güney Kutbu'na iki zıt ortamı yan yana koyan eşsiz bir özellik kazandırıyor:

- **Yüksek sırtlar ve krater kenarları:** Güneş neredeyse hiç batmıyor. Bu, güneş enerjisi için elverişli.
- **Derin krater tabanları:** Güneş hiç girmiyor. Bunlar kalıcı gölgeli bölgeler (PSR) ve buz barındırabilecek soğuk tuzaklar.

Shackleton Connecting Ridge tam olarak bu iki ortamın buluştuğu yerde bulunuyor. Bu yüzden Ay üssü için seçildi. Bizim için de en önemli ölçütleri bu durum belirliyor.

### 4.2 Sıcaklık ve arazi zorlukları

NASA, LRO'nun ilk ölçümlerini duyurduğu 2009 tarihli açıklamasında şu bulguları paylaştı:

- Diviner'ın ilk ölçümlerine göre kalıcı gölgeli kraterlerin geniş alanlarında sıcaklık yaklaşık eksi 400 °F (33 Kelvin). Bu, su buzunu veya hidrojeni milyarlarca yıl boyunca tutmaya yetecek kadar soğuk.
- LEND'in ilk sonuçlarına göre kalıcı gölgeli bölgeler ve çevreleri su ve hidrojen barındırabilir. NASA bunun doğrulanması için ek gözlem gerektiğini belirtiyor.
- LOLA verileri, bu bölgelerin keşfinin zor olacağını, çünkü arazinin çok engebeli olduğunu gösteriyor.

Bu üç bulgu, Dünya analoglarında arayacağımız özellikleri doğrudan tanımlıyor: çok soğuk, buz barındıran ve engebeli arazi. Dünya'da 33 Kelvin'e yaklaşan hiçbir doğal ortam yok. Bu nedenle sıcaklık ölçütü "mutlak benzerlik" değil, "göreli soğukluk ve kalıcı donma" olarak tanımlanmalı (Bölüm 13).

### 4.3 LRO ve aletleri

Lunar Reconnaissance Orbiter (LRO), Ay Güney Kutbu hakkındaki bilgilerimizin büyük kısmının kaynağı. NASA'nın Uzay Bilimi Veri Arşivi'ne (NSSDCA) göre LRO'nun en yüksek öncelikli ölçümleri şunlar: Ay yörüngesindeki derin uzay radyasyonu, küresel topografya, yüksek çözünürlüklü hidrojen haritalaması, kutuplardaki gölgeli bölgelerin sıcaklık haritalaması, kalıcı gölgeli bölgelerin görüntülenmesi, kutup soğuk tuzaklarındaki olası su buzunun tespiti, iniş yerleri için metre ölçeğindeki özelliklerin değerlendirilmesi ve kutup aydınlanma ortamının tanımlanması. NSSDCA'ya göre görevin temel amaçlarından biri, yerinde kaynak kullanımına (ISRU) uygun iniş yerleri bulmak.

Aşağıda her aletin ne ölçtüğü ve projemizde ne işe yarayacağı özetleniyor.

**LOLA (Lunar Orbiter Laser Altimeter).** NASA'ya göre LOLA iniş yerlerinin eğimini ve yüzey pürüzlülüğünü ölçüyor ve Ay'ın yüksek çözünürlüklü üç boyutlu haritalarını üretiyor. Yükseklik verilerini analiz ederek kalıcı olarak aydınlanan ve kalıcı olarak gölgede kalan alanları da belirliyor. LRO'nun genel tanıtım makalesine göre LOLA beş noktalı bir lazer deseniyle aynı anda beş profil ölçüyor. Her nokta yaklaşık 5 m çapında. Düşük eğimli bölgelerde yerel topografyayı yaklaşık 10 cm hassasiyetle verebiliyor.
*Projemizdeki kullanımı:* Hedef bölgenin eğim dağılımı, pürüzlülüğü, sırt ve krater biçimi ile aydınlanma modelleri için temel veri.

**Diviner (Diviner Lunar Radiometer Experiment, DLRE).** NASA'ya göre Diviner, buzu milyarlarca yıl boyunca koruyabilecek kadar soğuk alanları (soğuk tuzakları) ve olası buz yataklarını belirliyor. Ayrıca engebeli araziyi, kaya yoğunluğunu ve diğer iniş tehlikelerini de tanımlıyor. NASA'nın Moon to Mars Ay Yüzeyi Veri Kitabı'na göre Diviner gündüz ve gece sıcaklığını ölçen ilk alet. Dokuz farklı dalga boyu kullanarak 300 m kadar küçük alanlarda yüzey sıcaklığını yaklaşık 5 °C hassasiyetle belirleyebiliyor.
*Projemizdeki kullanımı:* Hedef bölgenin sıcaklık aralığı, gece-gündüz farkı ve soğuk tuzaklara yakınlığı.

**LAMP (Lyman-Alpha Mapping Project).** NASA'ya göre LAMP Ay yüzeyinin tamamını uzak morötesi ışıkta haritalıyor ve kutup bölgelerinde yüzey buzu ve kırağı arıyor. Kalıcı gölgeli bölgeleri yalnızca yıldız ışığıyla ve gezegenler arası hidrojenin yaydığı ışıkla aydınlanmış hâlde görüntüleyebiliyor.
*Projemizdeki kullanımı:* Hedef bölgedeki yüzey buzu göstergeleri. Dünya'da doğrudan karşılığı yok, ama "buzun yüzeye yakınlığı" ölçütünü tanımlamaya yardımcı oluyor.

**LEND (Lunar Exploration Neutron Detector).** NASA'ya göre LEND yüksek çözünürlüklü hidrojen dağılım haritaları çıkarıyor ve Ay'ın radyasyon ortamı hakkında bilgi sağlıyor. Ay yüzeyinde su buzu kanıtı aramak için kullanılıyor ve gelecekteki insanlı keşifler için yararlı ölçümler sunuyor. LEND'in tasarımı, Mars Odyssey'deki HEND aletine benziyor.
*Projemizdeki kullanımı:* Hedef bölgenin hidrojen (buz) zenginliği.

**Mini-RF (Miniature Radio Frequency).** NASA'ya göre Mini-RF'nin asıl amacı yeraltındaki su buzu yataklarını aramak. Kalıcı gölgeli bölgelerin yüksek çözünürlüklü radar görüntülerini de çekiyor. NASA'nın Haughton raporuna göre Mini-RF yandan bakan bir radar olduğu için tam kutupta bir "boşluk" bırakıyor. Örneğin Malapert Dağı görünürken Shackleton Krateri görünmüyor.
*Projemizdeki kullanımı:* Yeraltı buzu ve kaya dağılımı göstergeleri. Kutup boşluğu nedeniyle Shackleton için sınırlı kullanılabilir.

**LROC (Lunar Reconnaissance Orbiter Camera).** NASA'ya göre LROC'un iki dar açılı kamerası yaklaşık 1 m çözünürlükte siyah-beyaz görüntü çekiyor. Geniş açılı kamerası (WAC) ise Ay'ın tamamını yaklaşık 100 m çözünürlükte renkli ve morötesi görüntülüyor. LROC'un hedefleri arasında iniş yerlerinin metre ölçeğinde tanımlanması, kalıcı gölge ve aydınlık alanların haritalanması, neredeyse sürekli aydınlanan kutup tepelerinin yüksek çözünürlüklü haritalarının çıkarılması ve regolit özelliklerinin belirlenmesi var.
*Projemizdeki kullanımı:* Hedef bölgenin görsel tanımı, yüzey dokusu ve "astronotun göreceği manzara" karşılaştırması.

**CRaTER (Cosmic Ray Telescope for the Effects of Radiation).** NASA'ya göre CRaTER, doku eşdeğeri plastikler kullanarak arka plan uzay radyasyonunu inceliyor.
*Projemizdeki kullanımı:* Dünya'da Ay'daki radyasyonun karşılığı olmadığı için doğrudan bir ölçüt olmayacak. Ancak sunumda "Dünya analoglarının yapamadığı şeyler" bölümünde anılacak.

### 4.4 LRO verilerinin birlikte kullanımı

LRO'nun genel tanıtım makalesine göre Ay'daki su ve hidrojen kaynaklarına dair en kesin sonuçlar, tek bir aletten değil, bütün haritalama aletlerinin (Diviner, LAMP, LEND, LOLA ve LROC) birlikte analizinden çıkar. Bu ilke projemiz için de geçerli. Hedef profilimizi tek bir değişkenle değil, birden fazla aletin ortak resmiyle tanımlamalıyız:

| Hedef özellik | Birincil NASA verisi | Destekleyici NASA verisi |
|---|---|---|
| Aydınlanma süresi | LOLA (topografyadan aydınlanma modeli) | LROC WAC (zaman serisi görüntüler) |
| Kalıcı gölge | LOLA, LROC | LAMP |
| Yüzey sıcaklığı | Diviner | — |
| Buz ve hidrojen | LEND | LAMP, Mini-RF, Diviner (soğuk tuzaklar) |
| Eğim ve pürüzlülük | LOLA | LROC NAC |
| Yüzey görünümü | LROC NAC ve WAC | Artemis II görüntüleri |

### 4.5 Artemis III iniş bölgeleri ile Moon Base yeri arasındaki fark

NASA, Artemis III için Güney Kutbu yakınında güncellenmiş bir aday iniş bölgeleri listesi yayımladı. Bu bölgeler LRO verileri ve kapsamlı Ay bilimi araştırmaları kullanılarak seçildi. Bölgelerin bilimsel değeri, arazisi, aydınlanması ve Dünya ile iletişim koşulları değerlendirildi. NASA bu listenin nihai olmadığını, Güney Kutbu bölgesinin gelecekteki Artemis görevleri için taranmaya devam edeceğini belirtiyor.

Moon Base programı ise ilk robotik görev için **Shackleton Connecting Ridge**'i hedef olarak belirledi. Proje açısından bu ayrım şöyle önemli: Artemis III bölgeleri birer "iniş" hedefi, Shackleton Connecting Ridge ise bir "üs" hedefi. Görevin başlığı "kalıcı Ay üssü konumları" dediği için birincil hedefimiz Shackleton Connecting Ridge olmalı. Artemis III bölgeleri ise ikincil hedefler veya karşılaştırma için kullanılabilir.

---

## 5. Yeni açıklanan NASA verileri

### 5.1 Artemis II Ay bilimi verileri (7 Ekim 2026)

NASA, 7 Ekim 2026'da Artemis II görevinin Ay bilimi verilerini Planetary Data System'a (PDS) yükledi. NASA'nın açıklamasına göre bu veri paketi 800 GB'tan büyük ve bir kısmı daha önce hiç yayımlanmamıştı. Paketin içeriği:

- mürettebatın el kameralarından ve Orion uzay aracının kameralarından 11.000'den fazla tam çözünürlüklü fotoğraf ve video,
- mürettebatın Ay yüzeyine dair bilimsel gözlemlerinin 8,5 saatlik ses kaydı,
- mürettebatın üzerine not düştüğü görüntüler.

Verilerle birlikte üç belge de yayımlandı: Artemis II Ön Ay Bilimi Raporu, Artemis II Ay Bilimi Operasyonları Raporu ve Artemis II Ay Bilimi Veri Kullanıcı Kılavuzu. Gözlemler, görevin altıncı günü olan 6 Nisan 2026'daki Ay yakın geçişi sırasında yapıldı. NASA'nın Moon Base sayfasına göre Artemis II mürettebatı, Ay'ın en eski ve en büyük çarpma havzası olan Güney Kutbu–Aitken Havzası'nın yoğun kraterli doğu kenarını da görüntüledi.

**Projede nasıl kullanılabilir?** Artemis II görüntüleri yörüngeden değil, insan gözünden çekildi. Bu, projemize iki şey katıyor:

1. **Görsel karşılaştırma katmanı:** Önerdiğimiz Dünya analoğunun bir fotoğrafını, Artemis II mürettebatının çektiği bir Ay görüntüsünün yanına koyabiliriz. Bu, jüriye benzerliği sezgisel olarak gösterir.
2. **"Astronotun gördüğü" ölçütü:** Mürettebatın renk, doku ve ışık algısına dair notları, Dünya analoglarında astronot eğitimi için hangi görsel özelliklerin önemli olduğunu anlamamıza yardım edebilir.

**Sınırlılık:** Artemis II bir yakın geçiş görevi olduğu için görüntülerin hangi bölgeleri kapsadığı, özellikle de Shackleton Connecting Ridge'i içerip içermediği, PDS'teki kullanıcı kılavuzundan kontrol edilmeli. NASA'nın açıklaması bunu belirtmiyor.

### 5.2 Moon Base güncellemeleri (Mayıs – Kasım 2026)

Moon Base güncellemeleri doğrudan bir veri seti değil. Ancak bilimsel hedefleri ve konumları netleştirdikleri için projemiz açısından "hedef tanımı" verisi işlevi görüyorlar. Özellikle:

- Shackleton Connecting Ridge'in birincil hedef olarak belirlenmesi,
- VIPER'ın kalıcı gölgeli kraterlerde su buzunu haritalayacak olması,
- PROMISE'in kalıcı gölgeli bölgelerde ve uzun Ay gecelerinde çalışabilecek olması,
- MoonFall'ın yeraltı buzu arayacak olması,
- miniCAST'in güneş enerjisine dayalı olması.

Bu ayrıntılar, Ay üssü hedef profilimizin "buz + aydınlanma + engebeli arazi" üçlüsüne dayanmasının NASA'nın kendi önceliklerine uygun olduğunu gösteriyor.

### 5.3 EMIT'in genişletilmiş görevi

Dünya tarafında da yeni gelişmeler var. NASA'nın Earthdata kataloğuna göre EMIT aletinin mineral tanımlama ürünü (EMITL2BMIN) 2. sürümüyle güncellendi. Kataloğa göre EMIT'in asıl görevi kurak toz kaynağı bölgelerinin yüzey mineralojisini haritalamaktı. Genişletilmiş görevde ise uluslararası uzay istasyonunun yörüngesinden görülebilen bütün bölgelerden veri toplanıyor. Bu, Mars analoğu ararken mineral karşılaştırması yapabileceğimiz alanın genişlediği anlamına geliyor (Bölüm 12).

---

## 6. Mars tarafı: hedefler ve insanlı iniş ölçütleri

### 6.1 Neden Mars da hedefte?

Görev başlığı yalnızca Ay üssünü değil, Mars'ı da içeriyor. NASA'nın Moon Base sayfası, programın amaçlarından birinin gelecekteki Mars keşfine hazırlanmak olduğunu belirtiyor. PROMISE gezgininin Curiosity ve Perseverance'ın yedek parçalarıyla inşa edilecek olması da Ay ile Mars arasındaki teknoloji köprüsünü somutlaştırıyor. Bu yüzden projemizin Mars ayağı, Ay ayağından kopuk bir ek değil. Aynı yöntemin ikinci bir hedefe uygulanması.

### 6.2 Mars hedef seçenekleri

Mars için iki tür hedef seçebiliriz.

**Seçenek A – Bilimsel gezgin bölgeleri (Jezero ve Gale):**
- **Jezero Krateri:** Perseverance'ın inceleme yaptığı eski bir göl ve delta sistemi. NASA, Jezero'nun yaklaşık 3,5 milyar yıl önce bir göl ve nehir deltasına ev sahipliği yaptığını düşünüyor. MRO'nun spektral verileri, kraterin batı kenarında karbonat izleri gösteriyor. NASA'nın Mars Kampanyası belgesine göre Jezero'da birden fazla sulu dönemi işaret eden demir-magnezyum smektit killeri var.
- **Gale Krateri:** Curiosity'nin inceleme yaptığı krater. Ortasında yaklaşık 5 km kalınlığında tortul katmanlardan oluşan Aeolis Mons (Mount Sharp) var. NASA'nın 2015 insanlı iniş çalıştayına sunulan bir öneride Gale'in yaklaşık 4° güney enleminde ve 2 km'den alçak bir konumda olduğu, ancak yüzeye yakın su buzu bulma olasılığının düşük olduğu belirtiliyor.

**Seçenek B – İnsanlı üs bölgeleri (buz zengini orta enlemler):**
NASA'nın Mars'ta insanlı üs için önceliği suya erişim. NASA'ya göre Mars bilim insanlarının ve mühendislerinin çoğu, en erişilebilir yeraltı buzunun kuzey yarımkürede kutup bölgesinin hemen güneyinde olduğunu düşünüyor. Bu bölge Arcadia Planitia düzlüklerini ve buzullarla dolu Deuteronilus Mensae vadilerini kapsıyor. NASA'nın "Treasure Map" çalışmasına göre Arcadia Planitia'nın büyük bir bölümü, kuzey yarımkürede en cazip hedef. Haritada bu bölgede yüzeyden 30 cm'den daha sığ derinlikte su buzu görülüyor.

NASA'nın SWIM (Subsurface Water Ice Mapping) projesi, yüzeyin ilk 1 m'sindeki olası buz dağılımını gösteren haritalar üretiyor. NASA'ya göre ideal astronot iniş yerleri, buzun bulunduğu bölgenin en güney kenarında. Burası buzun var olacağı kadar kuzeyde, ama mümkün olan en sıcak sıcaklıkları sağlayacak kadar ekvatora yakın. Kuzey orta enlemler ayrıca daha kalın bir atmosfere sahip. Bu da iniş sırasında aracın yavaşlamasını kolaylaştırıyor.

### 6.3 NASA'nın insanlı iniş bölgesi ölçütleri

NASA'nın Mars Kampanyası belgesi, insanlı görevler için "Keşif Bölgesi" (Exploration Zone) kavramını şöyle tanımlıyor:

- Merkezi bir iniş yerinin yaklaşık **100 km** çevresindeki ilgi bölgelerinin toplamı,
- iniş ve kalkış teknolojileri nedeniyle orta ve düşük enlemler ile orta ve düşük yükseklikler tercih ediliyor,
- su buzuna erişim için ise daha yüksek enlemler tercih ediliyor,
- ön enlem sınırı **±50°**, yükseklik sınırı **2 km'den az**.

Aynı belgeye göre Jezero'da gün uzunluğu yaz gündönümünde yaklaşık 15 saat, kış gündönümünde yaklaşık 9 saat. Uç sıcaklıklar 20 °C'nin üstünden −110 °C'nin altına kadar uzanıyor. Mevsimsel değişimler ve periyodik toz fırtınaları da var.

### 6.4 Proje için Mars hedef önerisi

Projede iki Mars hedefini birlikte kullanmayı öneriyoruz:

1. **Jezero Krateri** – bilimsel (astrobiyoloji) analog arayışı için. Bunun Dünya'daki NASA onaylı karşılığı Salda Gölü (Bölüm 10.2).
2. **Arcadia Planitia** – insanlı üs (buz) analog arayışı için. Bu hedef, Ay üssü hedefimizle (Shackleton, buz ve üs) aynı mantığı taşıdığı için projeye tutarlılık kazandırıyor.

Zaman yetmezse yalnızca Jezero ile devam edilebilir. Çünkü Jezero için NASA'nın kullandığı bir Dünya analoğu (Salda) zaten mevcut ve bu doğrulama için çok değerli.

### 6.5 Mars hedeflerini ölçmek için NASA verileri

| Hedef özellik | NASA verisi | Açıklama |
|---|---|---|
| Topografya, eğim | MOLA (MGS), HiRISE ve CTX'ten üretilen yükseklik modelleri | Küresel ölçekte MOLA, yerel ölçekte HiRISE |
| Yüzey görüntüsü | CTX mozaiği (Mars Trek), HiRISE | Doku ve biçim karşılaştırması |
| Mineraller | MRO CRISM | Kil, sülfat, karbonat haritaları |
| Termal özellikler | Mars Odyssey THEMIS | Gece kızılötesi, termal atalet |
| Yeraltı buzu | SWIM haritaları (MRO ve Mars Odyssey verilerinden) | Buz derinliği ve dağılımı |
| Atmosfer | MRO MCS | Toz ve sıcaklık profilleri |
| Yüzey iklimi | Curiosity REMS, Perseverance MEDA | Sıcaklık, nem, basınç |
| Radyasyon | Curiosity RAD | Yüzey radyasyon dozu |

---

## 7. Analog kavramı: NASA'nın tanımı ve sınırları

### 7.1 NASA'ya göre gezegen analoğu nedir?

NASA'nın "Gezegen Analogları Hakkında Bilinmesi Gereken 10 Şey" sayfasına göre Dünya'daki bazı yerler o kadar uç koşullara sahip ki NASA bilim insanları bunları diğer dünyalardaki zorlu ortamları incelemek için yedek olarak kullanıyor. Bu yerler Ay'a, Mars'a, asteroitlere, hatta ötegezegenlere benzedikleri için "gezegen analoğu" olarak adlandırılıyor. Analog sahalar NASA'nın gelecekteki robotik ve insanlı görevlerini planlamasına ve bilim insanlarının Dünya'dan ayrılmadan uzak dünyaları araştırmasına yardımcı oluyor.

### 7.2 Üç analog türü

Aynı NASA sayfasına göre üç ana analog türü var:

1. **Jeolojik analoglar:** Başka bir gezegendeki jeolojik süreçlere veya yapılara benzeyen yerler. Örnek: İzlanda'daki volkanik araziler.
2. **Astrobiyoloji analogları:** Yaşamın sınırlarını incelemeye ve yaşam algılama araçlarını denemeye uygun yerler. Örnek: Atacama Çölü, Salda Gölü.
3. **Görev analogları:** İnsanlı ve robotik operasyonların, lojistiğin ve yalıtılmışlığın prova edildiği yerler. Örnek: Haughton-Mars Project.

Bu sınıflandırma projemiz için önemli. Çünkü bir yer bir türde çok iyi, başka bir türde zayıf bir analog olabilir. Puanlama modelimiz bu yüzden tek bir "benzerlik skoru" yerine, **görev türüne göre ağırlıklandırılmış** skorlar üretecek (Bölüm 13.5).

### 7.3 Bütün analoglar kısmidir

NASA kaynakları, hiçbir Dünya analoğunun hedefi birebir kopyalamadığını defalarca vurguluyor:

- NASA Astrobiyoloji Enstitüsü'nün Atacama yazısına göre Atacama, Mars kadar kuru ve soğuk değil. Aynı yazıda bir bilim insanı, Dünya'daki bütün benzetmelerin Mars'taki koşullardan çok daha zayıf kaldığını, Mars'ın çok daha kuru ve soğuk olduğunu ve UV ışınımının çok daha yoğun olduğunu söylüyor.
- NASA'nın 2005 tarihli Haughton-Mars Project raporuna göre Dünya'da Ay'ın veya Mars'ın ortamıyla tam olarak aynı olan bir yer yok. Ancak Haughton, büyük bir çarpma krateri içinde kayalık çöl arazisi ve çok çeşitli gezegen benzeri arazi türleriyle eşsiz bir birleşim sunuyor.
- NASA'nın Haughton üzerine 2011 tarihli raporu da Haughton'daki kayaların Ay malzemelerinden çok farklı olduğunu kabul ediyor. Buna rağmen çarpma etkisiyle yüzeye çıkmış temel kayaların, Ay'daki derin kabuk malzemelerinin nasıl yüzeye çıktığına dair ipuçları verdiğini belirtiyor.

**Proje için ilke:** Her aday için "neye benziyor" sorusunun yanında "neye benzemiyor" sorusu da yanıtlanmalı. Bu, hem bilimsel dürüstlük hem de jüri gözünde güvenilirlik sağlar.

### 7.4 Ay analoğu ile Ay üssü analoğu arasındaki fark

Bu ayrım raporun en önemli kavramsal noktalarından biri. "Ay'a benzeyen yer" ile "Ay üssüne benzeyen yer" aynı şey değil:

| | Ay'a benzeyen yer | Ay üssüne benzeyen yer |
|---|---|---|
| Aranan özellik | Çorak, volkanik veya kraterli görünüm | Kutup aydınlanması, buz, engebeli sırt-krater ilişkisi, yalıtılmışlık |
| Tipik örnekler | İzlanda yaylaları, Hawaii lav sahaları | Haughton Krateri, kutup çölleri |
| Kullanım amacı | Jeoloji eğitimi, örnek toplama | Üs operasyonları, kaynak arama, gezgin konvoyu, enerji planlama |
| Ekibin listesindeki karşılığı | Askja, Mauna Kea, Kapadokya, Bardenas | Yok |

Ekibin listesinin tamamı birinci sütuna giriyor. Görev ise ikinci sütunu istiyor. Bu yüzden listeyi genişletmek ve modele kutup ve buz ölçütlerini eklemek gerekiyor.

---

## 8. Başlangıç noktası: ekibin altı yer listesi

Projenin çıkış noktası, ekibin hazırladığı `ay-yuzeyine-benzeyen-yerler.md` dosyası oldu. Dosyanın başlığı "Dünya'da Ay Yüzeyini Andıran Yerler". Dosyada altı yer ve her biri için kısa bir açıklama var. Aşağıda dosyadaki ifadeler özetleniyor. Bunların NASA kaynaklarıyla karşılaştırılması Bölüm 9'da.

1. **Kapadokya (Türkiye):** Dosyaya göre volkanik patlamalar ve erozyonla oluşan peribacaları, krater benzeri oyuklar ve çölü andıran topografyasıyla Dünya'da Ay yüzeyine en çok benzetilen yerlerden biri.
2. **Wadi Rum (Ürdün):** Dosyaya göre halk arasında "Ay Vadisi" (Wadi al-Qamar) olarak biliniyor. Kızıl kumları ve büyük bazalt ve kumtaşı dağlarıyla yalnızca Ay'ı değil, bilimkurgu filmlerindeki Mars manzaralarını da andırıyor.
3. **Atacama Çölü / Valle de la Luna (Şili):** Dosyaya göre dünyanın en kurak yerlerinden biri. Kurumuş tuz gölleri, beyaz katmanları ve kıraç tepeleriyle NASA'nın Mars ve Ay araçlarını test ettiği bir simülasyon alanı.
4. **Askja Volkanı ve Yüksekleri (İzlanda):** Dosyaya göre aşırı yalıtılmış, bitki örtüsünden yoksun, siyah bazalt ve lav sahalarıyla kaplı bu bölge, Apollo astronotlarının Ay jeolojisine hazırlanması için eğitim alanı olarak kullanılmış.
5. **Mauna Kea (Hawaii, ABD):** Dosyaya göre bu sönmüş volkan, sarp yamaçları ve krater benzeri çukurlarıyla Ay yüzeyindeki kraterleri birebir simüle eden arazilere sahip.
6. **Bardenas Reales (Navarra, İspanya):** Dosyaya göre rüzgâr ve su erozyonunun şekillendirdiği killi ve tebeşirli çorak badlands yapısıyla Ay kraterlerini ve çorak düzlükleri hatırlatıyor.

### 8.1 Listenin güçlü yanları

- Liste farklı jeolojik ortamları kapsıyor: volkanik tüf (Kapadokya), kumtaşı ve granit (Wadi Rum), hiper-kurak tuzlu çöl (Atacama), bazaltik volkanizma (Askja, Mauna Kea) ve göl kökenli tortul badlands (Bardenas).
- Listede NASA'nın gerçekten kullandığı üç analog var: Askja, Mauna Kea ve Atacama.
- Liste farklı kıtalara yayılıyor. Bu, küresel bir puanlama modelinin doğrulanması için iyi bir çeşitlilik sağlıyor.

### 8.2 Listenin zayıf yanları

- Bütün yerler "Ay'a benzeyen yer" kategorisinde, hiçbiri "Ay üssüne benzeyen yer" kategorisinde değil (Bölüm 7.4).
- Kutup bölgesi yok. Buz veya kalıcı donmuş zemin içeren yer yok.
- Bazı ifadeler abartılı veya yanıltıcı. Örneğin Mauna Kea'nın "kraterleri birebir simüle ettiği" ya da Kapadokya'daki oyukların "krater benzeri" olduğu iddiaları (Bölüm 9).
- Atacama maddesinde turistik "Ay Vadisi" (Valle de la Luna) ile NASA'nın test yaptığı hiper-kurak çekirdek aynı yer gibi anlatılıyor.

---

## 9. Altı yerin ayrıntılı incelemesi

Bu bölümde her yer aynı şablonla inceleniyor:

- konum,
- NASA'nın bu yer hakkında ne söylediği,
- NASA'nın bu yeri analog olarak kullanıp kullanmadığı,
- Ay üssü ve Mars açısından uygunluğu,
- ekibin dosyasındaki ifadelerin düzeltilmesi,
- yeri ölçmek için kullanılacak NASA verileri,
- açık sorular.

Uygunluk notları ekibin niteliksel değerlendirmesidir. Koordinatlar yaklaşıktır ve analiz sırasında Landsat ve SRTM ile doğrulanacaktır.

### 9.1 Kapadokya (Türkiye)

**Konum:** Orta Anadolu, Nevşehir çevresi (yaklaşık 38,6° K, 34,8° D).

**NASA ne diyor?** NASA Earth Observatory'nin Göreme Milli Parkı yazısına göre:

- Kapadokya, Orta Anadolu'da yüksek ve kurak bir plato.
- Bölge zaman zaman "Ay manzarası" (moonscape) olarak tanımlanıyor.
- Yıllık yağış yaklaşık 38 cm. Bu miktar yazlık ve kışlık buğday gibi ürünleri desteklemeye yetiyor.
- Bölgedeki tüf yumuşak ve kolay işlenebilir olduğu için insanlar kayaları oyarak ev yapmış. Pencere, kapı ve kıvrımlı merdivenler açmışlar, hatta kayalara kiliseler oymuşlar.
- Göreme Milli Parkı 1985'te UNESCO Dünya Mirası listesine alınmış.
- Görüntü, Landsat 7 uydusunun ETM+ aletiyle 13 Ağustos 2002'de çekilmiş.

**NASA analog kullanımı:** NASA kaynaklarında Kapadokya için bir analog programı **bulunamadı**.

**Ay üssü uygunluğu: Düşük (●).** Kapadokya'nın oyukları çarpma kökenli değil, volkanik tüfün aşınmasıyla oluşmuş. Bölgede kutup aydınlanması, kalıcı gölge veya buz yok. Ayrıca NASA'nın tanımına göre bölgede tarım yapılıyor. Bu da Ay'ın bitkisiz yüzeyinden ciddi bir fark.

**Mars uygunluğu: Düşük–orta (●●).** Kurak, volkanik tüften oluşmuş bir plato olması Mars'taki bazı volkanik çökellerle genel bir benzerlik kuruyor. Ancak NASA'nın bu benzerliği inceleyen bir çalışması yok. Kayaya oyulmuş yerleşimler, radyasyondan korunan yeraltı yaşam alanları fikri için bir ilham kaynağı olabilir. Bu bir NASA analog bulgusu değil, ekibin fikri olarak sunulmalı.

**Dosyadaki düzeltmeler:**
- "Krater benzeri oyuklar" ifadesi yanıltıcı. Bu yapılar çarpma krateri değil.
- "Ay yüzeyine en çok benzetilen yerlerden biri" ifadesi popüler bir benzetme. NASA'nın bu yeri analog olarak kullandığına dair bir kayıt yok.

**Ölçmek için NASA verileri:** SRTM/NASADEM (eğim, pürüzlülük), Landsat (bitki örtüsü, NDVI), EMIT (mineral bileşimi), MERRA-2 ve GPM (kuraklık), MODIS (yüzey sıcaklığı).

**Açık sorular:**
- Kapadokya'nın bitki örtüsü ve tarım alanları, analog skorunu ne kadar düşürüyor?
- EMIT verisi, bölgedeki volkanik tüfün Mars'taki bir mineral imzasına benzediğini gösteriyor mu?

**Öneri:** Türkiye'den bir yer sunulacaksa NASA'nın resmi olarak kullandığı **Salda Gölü** çok daha güçlü bir aday (Bölüm 10.2). Kapadokya, modelin "görsel benzerlik ile ölçülmüş benzerlik arasındaki farkı" göstermek için iyi bir örnek olabilir.

### 9.2 Wadi Rum (Ürdün)

**Konum:** Güneybatı Ürdün (yaklaşık 29,6° K, 35,4° D).

**NASA ne diyor?** NASA Earth Observatory'nin 2001 tarihli yazısına göre:

- Güneybatı Ürdün'de alışılmadık bir manzara var. Granit ve kumtaşı dağlar, kızıl kumla dolu vadilerin yanında yükseliyor.
- Bazı dağlar deniz seviyesinden yaklaşık 1700 m yüksekliğe ulaşıyor. Birçoğunun yamacı neredeyse dikey.
- Granitin üzerinde Kambriyen ve Ordovisiyen dönemlerine ait kumtaşları ve gevşek kumlar bulunuyor.
- Manzara o kadar yabancı ki bölgeye "Ay Vadisi" deniyor. Bölge bir Mars filmine de set olmuş.
- Bölgede binlerce yıldır göçebe halklar yaşıyor. Bölge 1998'de koruma altına alındı.
- Görüntü, EO-1 uydusunun ALI aletiyle 27 Temmuz 2001'de çekilmiş.

NASA Earth Observatory'nin 2021 tarihli "Movie Mars on Earth" yazısına göre:

- *The Martian* (2015) filminin yönetmeni, filmdeki Mars sahnelerinde Wadi Rum'un manzarasını sık sık kullanmış.
- Landsat 8 görüntüsünde bölgenin renk ve dokuları Mars'takilere çok yakın görünüyor.
- Bölge başka filmlerde de Mars ya da başka çöl gezegenleri yerine kullanılmış.

**NASA analog kullanımı:** NASA kaynaklarında Wadi Rum için bilimsel bir analog programı **bulunamadı**. NASA'nın tanımı görsel benzerlik düzeyinde.

**Ay üssü uygunluğu: Düşük (●).** Kumtaşı ve granit Ay'ın anortositik kabuğundan ve bazaltlarından farklı. Kutup ve buz özellikleri yok.

**Mars uygunluğu: Orta–yüksek (●●●, görsel açıdan).** Renk ve doku benzerliği NASA tarafından da vurgulanıyor. Ancak bu benzerlik mineral düzeyinde EMIT verisiyle sınanmalı. Kızıl rengin kaynağı olan demir oksit (hematit, götit) EMIT'in temel olarak haritaladığı on mineral arasında. Dolayısıyla bu sınama doğrudan yapılabilir.

**Dosyadaki düzeltmeler:**
- "Ay Vadisi" adı doğru ve NASA kaynaklarıyla destekleniyor.
- Dosyadaki "bazalt dağları" ifadesi, NASA'nın tanımıyla uyuşmuyor. NASA dağları granit ve kumtaşı olarak tanımlıyor.

**Ölçmek için NASA verileri:** EMIT (demir oksit mineralleri), Landsat (renk ve doku, bitki örtüsü), SRTM/NASADEM (dik yamaçlar, vadiler), MERRA-2 (kuraklık).

**Açık sorular:**
- EMIT verisinde Wadi Rum'daki hematit ve götit oranı, Mars'taki tipik demir oksit imzasıyla karşılaştırılabilir mi?
- Görsel benzerliği yüksek ama jeolojik benzerliği düşük bir yeri modelde nasıl puanlamalıyız?

### 9.3 Atacama Çölü (Şili)

**Konum:** Kuzey Şili. NASA'nın testleri çölün hiper-kurak çekirdeğinde yapıldı (Yungay bölgesi, yaklaşık 24° G, 70° B).

**NASA ne diyor?**
- NASA Astrobiyoloji'nin saha listesine göre Atacama, dünyanın kutup dışındaki en kurak çölü ve **eski Mars için uygun bir analog**. Listede, ExoMars ve Icebreaker için planlananlara benzeyen uçuş prototipi bir gezgin ve matkap sisteminin Atacama'da kullanıldığı belirtiliyor.
- NASA'nın "Tire Tracks on Mars" sayfasına göre bölge, Mars'a benzeyen toprak kimyası, aşırı kuraklığı ve çok düşük canlılık düzeyi nedeniyle Mars koşullarının analoğu olarak kullanılıyor. Bu toprakta bakteri bile zor bulunuyor. Bu yüzden ARADS sisteminin uç bir ortamda yaşam arama yeteneğini test etmek için iyi bir yer.

**NASA analog kullanımı (doğrulandı):**
- **ARADS (Atacama Rover Astrobiology Drilling Studies):** NASA Astrobiyoloji Programı'nın PSTAR bileşeninden finanse edildi. İlk saha çalışması çölün hiper-kurak çekirdeğinde bir ay sürdü. NASA'ya göre bölge Mars'tan çok daha sıcak, ancak aşırı kuraklığı ve toprak kimyası Mars'a dikkat çekici ölçüde benziyor. Ekip şunları denedi:
  - Mars prototipi bir matkap,
  - bir örnek aktarım kolu,
  - Signs of Life Detector (SOLID),
  - 2007'de Phoenix görevinde uçan Wet Chemistry Laboratory'nin bir prototipi.
  
  NASA'ya göre proje, entegre bir gezgin, sondaj ve yaşam algılama sistemiyle Mars'ta yaşam arayan bir görevin teknik olarak mümkün olduğunu göstermeyi amaçlıyordu.
- **Life in the Atacama:** NASA'nın Zoë adlı gezgini 1 m'lik bir matkap taşıdı. Matkap, yeraltını o zamana kadar herhangi bir gezginin ulaştığından daha derinden inceledi.
- **Raman spektrometresi testi:** NASA'nın ASTEP programının desteklediği bir çalışmada Mars Micro-beam Raman Spectrometer, Zoë gezgini üzerinde 1 m derinlikten alınan sondaj örneklerini analiz etti.
- **JPL Chemical Laptop:** JPL'nin taşınabilir kimya laboratuvarı Atacama'da test edildi.

**Sınırlılıklar (NASA'ya göre):**
- NASA Astrobiyoloji Enstitüsü'nün yazısına göre Atacama Mars kadar kuru ve soğuk değil. Sıcaklık 0 ile 23 °C arasında değişiyor ve iklim ılıman, Akdeniz iklimine benziyor.
- Mars'ın ortalama sıcaklığı ise eksi 69 °C civarında.

**Ay üssü uygunluğu: Düşük–orta (●).** Atacama'nın çoraklığı ve bitkisizliği Ay'a görsel bir benzerlik veriyor. Ancak kutup, buz ve aydınlanma ölçütlerini karşılamıyor.

**Mars uygunluğu: Yüksek (●●●).** Listedeki en güçlü Mars analoğu. Özellikle kuraklık, toprak kimyası ve yaşam algılama testleri için.

**Dosyadaki düzeltmeler:**
- Dosya, turistik "Ay Vadisi" (Valle de la Luna) ile NASA'nın test sahasını aynı yer gibi anlatıyor. NASA kaynakları testlerin çölün hiper-kurak çekirdeğinde yapıldığını söylüyor. Valle de la Luna için ayrı bir NASA kaynağı bulunamadı.
- "Mars ve Ay araçlarının test edildiği" ifadesi kısmen doğru. NASA kaynaklarında Atacama'daki testler Mars için. Ay araçlarına dair bir test kaydı bulunamadı.

**Ölçmek için NASA verileri:** GPM IMERG ve MERRA-2 (yağış ve kuraklık), EMIT (sülfat, karbonat ve diğer mineraller), Landsat (bitkisizlik), MODIS (yüzey sıcaklığı), SRTM/NASADEM (topografya).

**Açık sorular:**
- Puanlama modeli, Atacama'nın hiper-kurak çekirdeğini çölün daha az kurak kısımlarından ayırt edebiliyor mu? Bu, modelin çözünürlüğünü test etmek için iyi bir ölçüt.

### 9.4 Askja Volkanı ve İzlanda Yaylaları

**Konum:** Orta İzlanda, Dyngjufjöll dağları (yaklaşık 65,0° K, 16,8° B).

**NASA ne diyor?**

*Apollo dönemi:*
- NASA'nın Apollo astronot jeoloji eğitimi kayıtlarına göre bir grup astronot 12–16 Temmuz 1965'te Orta İzlanda'da, Askja Kalderası yakınında eğitim aldı.
- 2–8 Temmuz 1967'deki ikinci İzlanda gezisinde Neil Armstrong da vardı.
- NASA tarih sayfasına göre Apollo 13 mürettebatından Swigert ve Haise, Temmuz 1967'de İzlanda'daki jeoloji gezisine katılmıştı. NASA'ya göre bitki örtüsü olmayan volkanik arazi Ay yüzeyini simüle etmek için idealdi.
- NASA'nın "Where No Man Has Gone Before" kitabının ekine göre astronotların jeoloji eğitimi için gittiği yerler arasında İzlanda, Meksika, New Mexico, Alaska ve Hawaii'deki volkanik bölgeler, Arizona'daki Grand Canyon ve Almanya'daki Ries Krateri vardı. Her sahanın Ay jeolojisine uygun özellikleri vardı ve her biri Ay'daki yüzey operasyonlarına benzer çalışmalar yapma fırsatı sunuyordu.

*Artemis dönemi:*
- NASA'ya göre İzlanda, Apollo döneminden beri astronot eğitimi için Ay'ın yerine kullanılıyor. Artemis II mürettebatı da bu geleneği sürdürdü.
- NASA'nın Artemis jeoloji eğitimi lideri Cindy Evans'a göre Apollo astronotları İzlanda'yı eğitim yerlerinin en çok Ay'a benzeyenlerinden biri olarak görüyordu. Evans'a göre İzlanda'da Ay'a benzer gezegen süreçleri (volkanizma), Ay'a benzeyen bir manzara ve astronotların Ay'da gözlemleyip keşfedeceği ölçekte arazi yapıları var.
- Mürettebat jeolojinin yanı sıra navigasyon ve keşif becerileri de çalıştı. Kaya örneği toplamak için çekiç, kepçe ve keski kullanmayı öğrendi.

*Ay Güney Kutbu bağlantısı (önemli):*
- NASA'nın Gezegen Analog Gezgini (Planetary Analog Explorer) sayfasına göre bilim insanları Askja yakınında **yer radarıyla gömülü buz** arıyor. Aynı teknik, gelecekte Ay Güney Kutbu yakınındaki kalıcı gölgeli bölgelerde su buzunu bulmak için kullanılacak.
- Aynı sayfa, İzlanda'nın Vikursundar bölgesindeki çakıllı yüzeyde oluşan büyük dalgacıkların izlendiğini belirtiyor. Bu dalgacıklar yalnızca en uç hava koşullarında hareket ediyor. Mars'ta da benzer sırtlar var, ama yaklaşık on kat daha büyük.

*Uzaktan algılama:*
- NASA'nın Terra uydusundaki ASTER aletiyle Askja çevresindeki buzul-volkanik çökeller haritalandı. Bu çalışma, Pleistosen dönemine ait buzul-volkanik tüfleri ve 1875 riyolitik patlamasının pomzasını hedefliyor.

**NASA analog kullanımı:** **Doğrulandı.** Apollo eğitimi, Artemis II eğitimi ve yeraltı buzu araştırması.

**Ay üssü uygunluğu: Orta (●●).** Volkanik jeoloji Ay'daki bazaltlara benziyor. Yeraltı buzu araştırması ise doğrudan Ay üssünün kaynak arama ihtiyacıyla ilgili. Ancak Ay üssünün kurulacağı Güney Kutbu bazaltik mare bölgesi değil. İzlanda'nın enlemi (yaklaşık 65° K) yazın uzun gün ışığı sağlıyor, ama bu Ay'ın kutup aydınlanmasıyla aynı şey değil.

**Mars uygunluğu: Orta–yüksek (●●).** Bazaltik volkanizma, buzul-volkan etkileşimi ve rüzgârla oluşan yüzey yapıları Mars için anlamlı.

**Dosyadaki düzeltmeler:** Dosyadaki ifade NASA kaynaklarıyla destekleniyor. Dosyaya Artemis II eğitimi ve yeraltı buzu araştırması eklenmeli.

**Ölçmek için NASA verileri:** ICESat-2 (İzlanda bölgesi ATL14 kapsamında), ASTER GDEM ve SRTM/NASADEM (İzlanda 60° kuzeyin üstünde kaldığı için SRTM kapsamaz; bu yüzden ASTER GDEM gerekli), Landsat (bitkisizlik), MODIS (yüzey sıcaklığı, kar örtüsü), ASTER (mineral ve termal).

**Açık sorular:**
- İzlanda'daki buzul-volkan etkileşimi, Ay üssü profilimizdeki "buz + engebeli arazi" ölçütüne ne kadar yaklaşıyor?

### 9.5 Mauna Kea (Hawaii, ABD)

**Konum:** Hawaii Büyük Ada (yaklaşık 19,8° K, 155,5° B).

**NASA ne diyor?**
- **2010 ve 2012 ISRU saha testleri:** NTRS'teki bir rapora göre Mauna Kea'daki 2010 ve 2012 testleri, NASA ile Kanada ve Almanya'daki ortak kurumların PISCES programı aracılığıyla yaptığı iş birliğiyle yürütüldü. Rapora göre sahadaki malzemenin ince taneli volkanik yapısı onu Ay ve Mars için uygun bir analog yapıyor. Kazı, saha hazırlığı ve kaynak kullanımı tekniklerinin denenmesinde kullanılıyor.
- **PISCES'in amacı:** NTRS'teki 2007 tarihli bir NASA belgesine göre PISCES'in uzun vadeli hedefi, Büyük Ada'da tam olarak simüle edilmiş bir Ay karakolu kurmak. Plana göre bu karakol yaşam alanları, yaşam desteği, enerji, iletişim ve ISRU işleme gibi temel sistemleri içerecek. Belge, Büyük Ada'nın Ay regolitini simüle edebildiğini de belirtiyor.
- **2012 ISRU görevi:** NASA'nın analog görevler sayfasının arşivlenmiş sürümüne göre 2012 görevinde araştırmacılar, su buzu ve uçucu maddeleri arayan ve tanımlayan robotik bir Ay kutup görevini simüle etti. Bilim operasyonları boyunca, bilim ve kaynak arama hedeflerini en iyi şekilde karşılamak için uzaktan operasyon stratejileri geliştirildi.

**NASA analog kullanımı:** **Doğrulandı.** ISRU ve robotik kaynak arama testleri.

**Ay üssü uygunluğu: Orta–yüksek (●●).** Mauna Kea'nın asıl değeri, Ay üssünün oksijen ve su ihtiyacına yönelik ISRU teknolojilerinin denenmesi. 2012'deki Ay kutup görevi simülasyonu, Ay üssüyle doğrudan ilgili. Ancak Mauna Kea kendisi kutup ortamı değil.

**Mars uygunluğu: Orta (●●).** Volkanik malzeme ve ISRU testleri Mars için de geçerli.

**Dosyadaki düzeltmeler:**
- "Ay kraterlerini birebir simüle eden arazi" ifadesi **abartılı**. NASA kaynaklarına göre Mauna Kea'nın analog değeri krater biçiminden değil, **regolite benzeyen ince taneli volkanik malzemeden** geliyor.
- Dosyaya ISRU testleri ve 2012 Ay kutup görevi simülasyonu eklenmeli.

**Ölçmek için NASA verileri:** SRTM/NASADEM (topografya), Landsat (bitki örtüsü), EMIT (volkanik mineraller, 52° K–G aralığında olduğu için kapsanıyor), MODIS (yüzey sıcaklığı).

**Açık sorular:**
- Modelimiz "ISRU testine uygunluk" diye ayrı bir ölçüt içermeli mi? Bu ölçütün bir göstergesi, ince taneli gevşek malzemenin varlığı olabilir.

### 9.6 Bardenas Reales (Navarra, İspanya)

**Konum:** Kuzeydoğu İspanya (yaklaşık 42,2° K, 1,5° B).

**NASA ne diyor?** NASA'nın Astronomy Picture of the Day (APOD) sayfasındaki 2 Eylül 2013 tarihli görüntü, Bardenas Reales'teki Castildetierra kaya oluşumunu tanıtıyor. Sayfaya göre:

- Bardenas Reales, kuzeydoğu İspanya'da doğal bir badlands (kötü arazi) bölgesi.
- Castildetierra yaklaşık 50 m yüksekliğinde bir kaya kulesi. Binlerce yıllık rüzgâr ve su aşınmasından geriye kalmış kil ve kumtaşından oluşuyor.

**NASA analog kullanımı:** NASA kaynaklarında Bardenas Reales için bir analog programı **bulunamadı**.

**Ay üssü uygunluğu: Düşük (●).** Kil ve kumtaşı Ay'ın yüzey malzemesinden çok farklı. Kutup, buz ve aydınlanma özellikleri yok.

**Mars uygunluğu: Orta (●●).** Rüzgâr ve su aşınmasıyla oluşmuş biçimler ve kil içeriği, Mars'taki tortul yapılarla genel bir benzerlik taşıyor. Bu, EMIT'in kil minerallerini (kaolinit, montmorillonit, illit) haritalayabilmesi sayesinde sınanabilir.

**Dosyadaki düzeltmeler:**
- Dosyadaki "killi" ifadesi NASA APOD'un tanımıyla uyumlu.
- "Tebeşirli" ifadesi için NASA kaynaklarında bir destek bulunamadı.
- "Ay kraterlerini hatırlatır" ifadesi görsel bir benzetme. Bardenas'ta çarpma krateri yok.

**Ölçmek için NASA verileri:** EMIT (kil mineralleri), Landsat (bitki örtüsü ve doku), SRTM/NASADEM (aşınma biçimleri, eğim), MERRA-2 (kuraklık).

**Açık sorular:**
- Bardenas yarı-kurak bir bölge ve çevresi tarım alanlarıyla çevrili. Bu durum, Landsat bitki örtüsü ölçütünde skorunu ne kadar düşürüyor?

---

## 10. NASA'nın kullandığı ek analoglar

Ekibin listesindeki boşlukları doldurmak için, NASA'nın kendi kaynaklarında analog olarak kullandığı yerleri inceledik. Bu yerler hem doğrulama setimizi güçlendiriyor hem de "kutup ve buz" boşluğunu kapatıyor.

### 10.1 Haughton Krateri, Devon Adası (Kanada) – Ay üssünün eksik halkası

**Konum:** Nunavut, Kanada (yaklaşık 75° K, 90° B).

**NASA ne diyor?**
- NASA'nın "Gezegen Analogları Hakkında 10 Şey" sayfasına göre Haughton-Mars Project bir **görev analoğu**. Devon Adası dünyanın en büyük ıssız adası. Çorak arazisi, dondurucu sıcaklıkları, yalıtılmışlığı ve uzaklığı, Mars'taki ve diğer gezegen hedeflerindeki koşullara benziyor. Mars kraterlerle kaplı olduğu için Haughton Krateri, Mars'taki uzay yürüyüşlerini (EVA) prova etmek için iyi bir yer.
- NASA'nın analog görevler bilgi notuna göre Haughton'a yalnızca Kanada'daki Resolute Bay'den uçakla ulaşılabiliyor. Kayalık arktik çöl ortamı, jeolojik özellikleri ve biyolojik nitelikleri, Mars'a yapılacak olası robotik ve insanlı görevlerin gereksinimlerini toplamak için en uygun ortamı sağladı. NASA ve ortak kuruluşlarının bilim insanları ve mühendisleri burada temsili Ay bilimi ve keşif faaliyetleri yürütüyor.

**Ay üssü bağlantısı (NASA/TM-2011-216157):** NASA'nın 2011 tarihli teknik raporu, Haughton Krateri'ni açıkça bir **Ay analog sahası** olarak değerlendiriyor:

- Haughton-Mars Project araştırma istasyonu krater kenarında kurulu. Rapora göre bu, Shackleton Krateri'nde kurulacak bir Ay karakolunun konumuna çok benziyor.
- İstasyon, birkaç bin kilometrekarelik alandaki tek altyapı. Bu yüzden basınçlı gezginlerle yapılacak keşif yolculukları için bir Ay üssü analoğu işlevi görebiliyor.
- Haughton'daki kayalar Ay malzemelerinden çok farklı. Ancak çarpmayla yüzeye çıkmış temel kayalar, Ay'daki derin kabuk malzemelerinin tekrarlanan çarpmalarla nasıl yüzeye çıkmış olabileceğine dair ipuçları sunuyor.
- Raporda, Ay yörüngesinden elde edilebilecek veri türlerini taklit eden uzaktan gözlem veri setleriyle bir gezgin rota planlama deneyi yapıldığı anlatılıyor.

**2010 simülasyonu:** NASA'nın analog testleri blogundaki 2010 tarihli yazıya göre HMP-2010 sırasında araştırmacılar, Haughton Krateri'ni kullanarak Ay'ın güney kutup bölgesindeki **Shackleton Krateri'nden Malapert Dağı'na** uzanan yaklaşık 75 millik (yaklaşık 120 km) bir robotik konvoyu simüle etti. Bu, Ay üssü bölgesinin Dünya'daki provasına çok somut bir örnek.

**Yaş:** NTRS'teki bir çalışmaya göre Haughton'un yaşı yeni ölçümlerle yaklaşık **38 milyon yıl** (Eosen) olarak belirlendi. Daha önceki tahminler Miyosen yaşını gösteriyordu. Raporun önceki sürümlerinde yer alan "23 milyon yıl" bilgisi bu yüzden düzeltildi.

**Mars bağlantısı:** NTRS'teki 2000 tarihli bir çalışmaya göre Devon Adası'nda, Mars'taki bazı küçük vadilere biçim olarak benzeyen vadi ağları var. Ancak bu vadiler Mars'taki karşılıklarından yaklaşık iki kat büyüklük mertebesi daha küçük.

**Değerlendirme:**
- Ay üssü uygunluğu: **Yüksek (●●●).** Kutup ortamı, krater kenarındaki üs konumu ve Shackleton–Malapert simülasyonu.
- Mars uygunluğu: **Yüksek (●●●).**
- **Ölçmek için NASA verileri:** ICESat-2 (Kuzey Kanada Arktiği bölgesi), ASTER GDEM, Landsat 7 ve 8, MODIS (kar ve buz örtüsü, yüzey sıcaklığı). SRTM bu enlemi kapsamıyor.

### 10.2 Salda Gölü (Burdur, Türkiye) – Jezero'nun NASA onaylı analoğu

**Konum:** Güneybatı Türkiye, Burdur.

**NASA ne diyor?**
- NASA Earth Matters yazısına göre Salda Gölü ile Mars'taki Jezero Krateri benzer mineraloji ve jeolojiye sahip. NASA'ya göre Salda, Jezero'da bulunanlara benzeyen **karbonat mineralleri ve delta çökelleri** barındıran, dünyada bilinen tek göl.
- Gölün beyaz kıyısı, Jezero'da tespit edilen karbonat minerallerine benzeyen **hidromagnezit** içeren kum ve çakıllardan oluşuyor. Bu tortulların, mikropların yardımıyla oluşan büyük **mikrobiyalit** tepeciklerinden aşındığı düşünülüyor.
- NASA'nın "Jez like Mars" yazısına göre Jezero görüntüsü MRO'nun Context Camera (CTX) aletinden, Salda görüntüsü ise 8 Haziran 2020'de Landsat 8'in OLI aletinden alındı. Gölde, çevredeki ana kayadan aşınıp taşınan kaya parçalarıyla dolu alüvyon yelpazeleri var. Bunlar Jezero'daki deltaya benziyor.
- Perseverance'ın bilim ekibinden bir gezegen bilimci ve öğrencileri 2019 yazında Salda'da saha çalışması yaptı.
- JPL'ye göre Salda'nın kıyısındaki kayalar, sudaki mineralleri ve tortulları yakalayan mikroplar tarafından zaman içinde oluşturuldu. Bu mikrobiyalitler, Dünya'daki en eski fosil yaşam kayıtlarından bazılarını içeriyor.

**NASA analog kullanımı:** **Doğrulandı.** NASA'nın Gezegen Analog Gezgini sayfasında "Yaşam Arayışı: Türkiye ve Mars" başlığıyla yer alıyor.

**Değerlendirme:**
- Ay üssü uygunluğu: **Düşük (●).**
- Mars uygunluğu: **Yüksek (●●●).** Özellikle Jezero hedefi için.
- **Türkiye açısı:** Projede Türkiye'den bir yer öne çıkarılacaksa en güçlü seçenek bu. Hem NASA'nın kendi kaynaklarıyla destekleniyor hem de modelin doğrulama setinde "bilinen pozitif" olarak kullanılabilir.
- **Ölçmek için NASA verileri:** EMIT (karbonat mineralleri), Landsat (göl kıyısı, delta), SRTM/NASADEM (topografya).

### 10.3 McMurdo Kuru Vadileri ve University Valley (Antarktika)

**NASA ne diyor?** NASA Astrobiyoloji'nin saha listesine göre Antarktika, Dünya'nın bilinen en soğuk ve en kuru ortamlarından bazılarını barındırıyor ve uzun süredir eski Mars için analog olarak kullanılıyor. McMurdo Kuru Vadileri'ndeki University Valley'de, Mars'ın bazı bölgelerinde bulunana benzeyen, buzla çimentolanmış yeraltı zemini var.

**Değerlendirme:** Ay üssü uygunluğu yüksek (kutup ortamı, buz), Mars uygunluğu yüksek (buzla çimentolanmış zemin). Ölçmek için ICESat-2 (Antarktika ATL14 kapsamında), Landsat ve MODIS kullanılabilir.

### 10.4 Death Valley (Kaliforniya, ABD)

**NASA ne diyor?** NASA'nın Gezegen Analog Gezgini sayfasına göre Death Valley, Mars'taki Utopia Planitia'ya benziyor. Mars 2020 Perseverance ekibi burada tehlikelerden kaçınma çalışmaları yaptı.

**Değerlendirme:** Mars uygunluğu yüksek (gezgin operasyonları için).

### 10.5 Kilauea (Hawaii, ABD)

**NASA ne diyor?** NASA'nın Gezegen Analog Gezgini sayfasına göre Kilauea'nın yamaçlarında araştırmacılar, küçük bir jeolog ve astronot ekibinin benzer görevleri Ay yüzeyinde ne kadar sürede yapacağını test ediyor. Sayfada bu ikili "Bazalt Manzaraları: Kilauea ve Ay" başlığıyla yer alıyor.

**Değerlendirme:** Ay (genel) uygunluğu yüksek. Ay üssü uygunluğu düşük, çünkü bölge kutupta değil.

### 10.6 Medicine Lake Volkanı lav mağaraları (Kaliforniya, ABD)

**NASA ne diyor?** NASA'nın Gezegen Analog Gezgini sayfasına göre Medicine Lake Volkanı yakınındaki lav mağaraları ileride astronotları radyasyondan koruyabilecek türden yerlere benziyor. Bilim insanları, gizli mağaraları yukarıdan tespit etmenin yollarını araştırıyor.

**Değerlendirme:** Görev metninde "mağaralar" ayrıca anıldığı için bu analog önemli. Projede "yeraltı habitatı" ölçütü eklenirse, bu yer bir doğrulama noktası olabilir.

### 10.7 Pilot Valley (Utah, ABD)

**NASA ne diyor?** NASA'nın Gezegen Analog Gezgini sayfasına göre Utah'taki Pilot Valley'deki tuzlarda perklorat bulunuyor. Perklorat Mars'ta da gözlendi ve yaşanabilirliğe işaret edebilir.

**Değerlendirme:** Mars kimyası açısından uygunluğu yüksek.

### 10.8 Verde Valley (Arizona, ABD)

**NASA ne diyor?** NASA'nın Gezegen Analog Gezgini sayfasına göre Verde Valley'deki araştırmalar, biyolojik izlerin nasıl korunduğunu anlamaya yardımcı oluyor. Bu bilgi, Curiosity'nin Mars'ta neyi aradığını yönlendiriyor.

### 10.9 Katmai, On Bin Duman Vadisi (Alaska, ABD)

**NASA ne diyor?** NASA Earth Observatory'nin 24 Haziran 2026 tarihli yazısına göre Apollo astronotları 1965 ve 1966 yazlarında Alaska'daki Katmai Milli Parkı'na giderek Ay'a benzeyen ortamlarda saha jeolojisi simülasyonları yaptı. Astronotlar "Ay oyunu" (Moon game) adını verdikleri bir alıştırmada ikişer kişilik gruplar hâlinde tanımadıkları sahalara bırakıldı ve Ay'daymış gibi davranmaları istendi. Görevleri temsili jeolojik örnekler toplamak ve gözlemlerini bilim insanlarına aktarmayı çalışmaktı. NASA'ya göre bu vadideki volkanik arazi Ay'daki eski lav akıntılarından çok daha taze, ama astronotlara volkanik malzemeleri neredeyse bozulmamış hâlde görme fırsatı sundu.

### 10.10 Mojave Çölü (ABD)

**NASA ne diyor?** NASA Astrobiyoloji'nin saha listesine göre Mojave Çölü uç sıcaklık farklarıyla biliniyor. Bu yüzden Mars gibi Dünya dışı ortamlar için iyi bir analog sayılıyor.

---

## 11. Toplu karşılaştırma

Aşağıdaki tablo, ekibin altı yerini ve NASA'nın kullandığı başlıca ek analogları yan yana koyuyor. Puanlar ekibin niteliksel değerlendirmesidir: ●●● yüksek, ●● orta, ● düşük. Model kurulduğunda bu tablonun yerini veriyle hesaplanmış skorlar alacak.

| Yer | Kaynak | NASA analog kullanımı | Ay (genel) | **Ay üssü (kutup + buz)** | Mars | NASA kaynaklarına göre güçlü yanı |
|---|---|---|---|---|---|---|
| Kapadokya | Ekip listesi | Bulunamadı | ● | ● | ●● | Kurak volkanik tüf platosu |
| Wadi Rum | Ekip listesi | Bulunamadı (görsel tanım var) | ●● | ● | ●●● (görsel) | Mars'a benzeyen renk ve doku |
| Atacama | Ekip listesi | ARADS, Life in the Atacama | ●● | ● | ●●● | Kuraklık, toprak kimyası, yaşam algılama |
| Askja / İzlanda | Ekip listesi | Apollo, Artemis II, yeraltı buzu | ●●● | ●● | ●● | Astronot eğitimi; PSR buzu aramaya benzer radar çalışması |
| Mauna Kea | Ekip listesi | ISRU testleri (2010, 2012) | ●●● | ●● | ●● | Regolit benzeri malzeme, Ay kutup görevi simülasyonu |
| Bardenas Reales | Ekip listesi | Bulunamadı | ● | ● | ●● | Aşınma biçimleri, kil |
| **Haughton** | NASA | HMP, 2010 Shackleton–Malapert simülasyonu | ●●● | **●●●** | ●●● | Kutup çölü, krater kenarında üs |
| **Salda Gölü** | NASA | Perseverance / Jezero analoğu | ● | ● | **●●●** | Jezero'ya benzeyen karbonat ve delta yapıları |
| **McMurdo Kuru Vadileri** | NASA | Astrobiyoloji saha listesi | ●● | ●●● | ●●● | En soğuk ve kuru ortam, buzla çimentolanmış zemin |
| **Death Valley** | NASA | Mars 2020 tehlikeden kaçınma çalışması | ●● | ● | ●●● | Gezgin operasyonları |
| **Kilauea** | NASA | Ay saha operasyonu zaman testleri | ●●● | ● | ●● | Bazalt manzarası |
| **Medicine Lake** | NASA | Lav mağaraları | ●● | ●● (yeraltı korunağı) | ●● | Radyasyondan korunma için mağara |

### 11.1 Tablodan çıkan sonuçlar

1. **Ay üssü sütunu boşluğu:** Ekibin altı yerinden hiçbiri Ay üssü sütununda ●●● almıyor. Bu sütunda yüksek puan alan yerler yalnızca kutup bölgelerinde: Haughton ve McMurdo Kuru Vadileri.
2. **Mars sütunu zenginliği:** Mars için güçlü analoglar çok daha fazla ve çeşitli: Atacama (kuraklık), Salda (karbonat ve delta), Death Valley (gezgin operasyonları), McMurdo (soğuk ve buz).
3. **Doğrulama setinin dengesi:** Doğrulama setimiz hem Ay üssü hem Mars için en az iki-üç güçlü pozitif örnek içermeli. Tablo bunun mümkün olduğunu gösteriyor.
4. **Yeni aday arayışının yönü:** Ay üssü için yeni adaylar büyük olasılıkla yüksek enlemlerde (Arktik ve Antarktika çevresi, yüksek dağlar) çıkacak. Mars için ise orta enlem çölleri, tuz düzlükleri ve volkanik alanlarda çıkacak.

---

## 12. Dünya tarafındaki NASA veri katmanları

Bu bölüm, Dünya'yı puanlamak için kullanılacak NASA veri setlerini ayrıntılı olarak tanımlıyor. Her veri seti için ne ölçtüğü, kapsamı ve projedeki kullanımı veriliyor.

### 12.1 Yükseklik ve topografya

**SRTMGL1 ve NASADEM.** NASA'nın Earthdata kataloğuna göre SRTM yaklaşık 30 m çözünürlükte yükseklik verisi sağlıyor ve 60° kuzey ile 56° güney enlemleri arasındaki karaları kapsıyor. NASADEM, SRTM'nin yeniden işlenmiş sürümü ve aynı kapsama sahip.
- *Projedeki kullanımı:* Eğim, pürüzlülük, yerel kabartı (relief), sırt ve krater biçimlerinin tespiti.
- *Sınırlılık:* 60° kuzeyin üstünü kapsamıyor. Bu yüzden Haughton (yaklaşık 75° K), İzlanda'nın büyük kısmı (yaklaşık 65° K) ve Antarktika için kullanılamıyor.

**ICESat-2 ATL14.** NASA Earthdata kataloğuna göre ATL14, Antarktika buz tabakası ve Arktik çevresindeki bölgeler için 100 m çözünürlüklü, ızgaralı bir sayısal yükseklik modeli sağlıyor. Ürün 2019'dan bugüne uzanıyor ve NASA'nın NSIDC DAAC arşivinde. Algoritma belgesine göre ürün şu bölgeler için üretiliyor: Antarktika, Grönland ve çevresindeki buz takkeleri, Kuzey Kanada Arktiği, Güney Kanada Arktiği, İzlanda, Svalbard ve Rusya Arktiği.
- *Projedeki kullanımı:* Kutup analogları için yükseklik ve buz yüzeyi verisi.
- *Sınırlılık:* ATL14 bir **kara buzu** ürünü. Algoritma belgesine göre veri noktaları buzul maskeleri kullanılarak seçiliyor. Bu yüzden Haughton gibi **buzsuz** kutup çöllerini tam kapsamayabilir. Bu boşluk ASTER GDEM ile doldurulmalı.

**ASTER GDEM.** NASA'nın Terra uydusundaki ASTER aletinden üretilen küresel yükseklik modeli. SRTM'nin kapsamadığı yüksek enlemleri de kapsıyor. ASTER, NASA ile Japonya'nın ortak geliştirdiği bir alet; veri NASA'nın LP DAAC arşivinden dağıtılıyor.
- *Projedeki kullanımı:* 60° kuzeyin üstündeki buzsuz alanların (Haughton gibi) topografyası.

### 12.2 Yüzey görüntüsü ve bitki örtüsü

**Landsat ve HLSL30.** Landsat uyduları yaklaşık 30 m çözünürlükte çok bantlı yüzey görüntüleri sağlıyor. HLS (Harmonized Landsat Sentinel-2) ürününün yalnızca Landsat kısmı olan HLSL30 kullanılacak. Böylece NASA dışı uydu verisi devreye girmemiş olacak.
- *Projedeki kullanımı:* Bitki örtüsü indeksi (NDVI), yüzey rengi ve dokusu, su varlığı.
- *Örnek:* NASA Earth Observatory'nin Salda Gölü ve Wadi Rum karşılaştırmaları Landsat 8 görüntüleriyle yapıldı. Bu, Landsat'ın analog tanımlamada NASA'nın kendi kullandığı bir veri olduğunu gösteriyor.

### 12.3 Mineraller

**EMIT (Earth Surface Mineral Dust Source Investigation).** NASA'nın Earthdata kataloğu ve EMIT tanıtım sayfaları şu bilgileri veriyor:

- EMIT, Uluslararası Uzay İstasyonu'na yerleştirilmiş bir görüntüleme spektrometresi. 14 Temmuz 2022'de fırlatıldı.
- Asıl görevi, kurak toz kaynağı bölgelerinin yüzey mineralojisini görünür ve kısa dalga kızılötesi aralığında haritalamak.
- 75 km genişliğinde bir şerit görüyor, 285 spektral bant kullanıyor ve 60 m çözünürlüğe sahip.
- Asıl görevde 52° kuzey ile 52° güney enlemleri arasındaki kurak bölgelere odaklandı. Genişletilmiş görevde uzay istasyonunun yörüngesinden görülebilen bütün bölgelerden veri topluyor.
- Mineral tanımlama ürünü (EMITL2BMIN) on temel minerale odaklanıyor: **kalsit, klorit, dolomit, götit, alçıtaşı, hematit, illit+muskovit, kaolinit, montmorillonit ve vermikülit**.

*Projedeki kullanımı:* Mars analoğu ararken mineral benzerliği.
- Demir oksitler (hematit, götit): Mars'ın kızıl rengiyle ilgili. Wadi Rum için doğrudan sınama yapılabilir.
- Killer (kaolinit, montmorillonit, illit): Jezero'daki killerle karşılaştırma.
- Karbonatlar (kalsit, dolomit): Jezero'daki karbonatlarla karşılaştırma. Salda için sınama yapılabilir.
- Sülfatlar (alçıtaşı): Mars'taki sülfat çökelleriyle karşılaştırma. Atacama için sınama yapılabilir.

*Sınırlılık:* Kutup bölgelerini kapsamıyor. Bu yüzden Ay üssü puanında kullanılmayacak.

*Ek bilgi:* EMIT'in tasarımı, NASA'nın daha önce Ay'da (M³) ve Mars'ta (CRISM) kullandığı görüntüleme spektroskopisi geleneğine dayanıyor. Bu, EMIT ile CRISM arasında yapılacak bir karşılaştırmayı yöntem açısından anlamlı kılıyor.

### 12.4 Sıcaklık ve iklim

**MODIS yüzey sıcaklığı (LST).** NASA'nın Terra ve Aqua uydularındaki MODIS aletinden üretilen kara yüzeyi sıcaklığı ürünü. Gece ve gündüz sıcaklıkları ayrı ayrı veriliyor.
- *Projedeki kullanımı:* Yıllık ortalama sıcaklık, gece-gündüz farkı, donma günü sayısı. Ay üssü profili için "göreli soğukluk", Mars profili için "sıcaklık aralığı".

**MODIS kar ve buz örtüsü.** Kar ve buz örtüsünün zaman içindeki kalıcılığı.
- *Projedeki kullanımı:* Ay üssü profili için "kalıcı buz veya kar" göstergesi.

**MERRA-2.** NASA'nın Goddard Uzay Uçuş Merkezi'nin ürettiği atmosferik yeniden analiz veri seti. Sıcaklık, nem, rüzgâr ve yüzey yansıtıcılığı (albedo) gibi değişkenler içeriyor.
- *Projedeki kullanımı:* Uzun dönemli iklim ortalamaları, kuraklık göstergeleri, rüzgâr.

**GPM IMERG.** NASA'nın Küresel Yağış Ölçümü görevinden üretilen yağış verisi.
- *Projedeki kullanımı:* Kuraklık. Mars profilinde en önemli değişkenlerden biri.

### 12.5 Yalıtılmışlık

**NASA Black Marble (gece ışıkları).** NASA'nın gece ışıkları ürünü, insan yerleşimlerinin bir göstergesi olarak kullanılabilir. NASA Earth Observatory, bu ürünü 2023 Türkiye depremlerinden sonra elektrik kesintilerini izlemek için kullandı.
- *Projedeki kullanımı:* Yalıtılmışlık ölçütü. Gece ışığı ne kadar azsa, yer o kadar yalıtılmış. Bu, "görev analoğu" türü için önemli.

### 12.6 Ay ve Mars hedef verileri

| Gök cismi | Veri | Erişim |
|---|---|---|
| Ay | LRO LOLA, Diviner, LAMP, LEND, Mini-RF, LROC | NASA PDS; NASA Moon Trek |
| Ay | Artemis II görüntüleri | NASA PDS (Ekim 2026) |
| Mars | MOLA, CTX, HiRISE | NASA PDS; NASA Mars Trek |
| Mars | CRISM | NASA PDS |
| Mars | THEMIS, MCS | NASA PDS |
| Mars | SWIM buz haritaları | NASA / JPL |
| Mars | REMS, MEDA, RAD | NASA PDS |

### 12.7 Veri katmanlarının özet tablosu

| Ölçüt | Dünya verisi | Ay hedef verisi | Mars hedef verisi |
|---|---|---|---|
| Eğim ve pürüzlülük | SRTM/NASADEM, ASTER GDEM, ICESat-2 | LOLA | MOLA, HiRISE |
| Sırt ve krater biçimi | SRTM/NASADEM, ASTER GDEM | LOLA, LROC | MOLA, CTX |
| Aydınlanma | Enlem ve gün uzunluğu (hesaplanır) | LOLA aydınlanma modelleri | Enlem |
| Sıcaklık | MODIS LST, MERRA-2 | Diviner | THEMIS, REMS, MEDA |
| Buz | MODIS kar/buz, ICESat-2 | LEND, LAMP, Mini-RF, Diviner | SWIM |
| Kuraklık | GPM IMERG, MERRA-2 | — (Ay'da atmosfer yok) | REMS, MEDA |
| Mineraller | EMIT | LROC WAC (genel) | CRISM |
| Bitkisizlik | Landsat NDVI | — (her yer bitkisiz) | — (her yer bitkisiz) |
| Yalıtılmışlık | Black Marble | — | — |

---

## 13. Yöntem: puanlama modeli

### 13.1 Genel yaklaşım

Model her kara hücresini iki hedef profile göre puanlayacak: **Ay üssü profili** ve **Mars profili**. Her profil, Bölüm 12'deki ölçütlerden oluşan bir "özellik vektörü" ile tanımlanacak. Bir Dünya hücresinin skoru, kendi özellik vektörünün hedef profile ne kadar yakın olduğunu gösterecek.

Modelin üç temel ilkesi var:

1. **Açıklanabilirlik:** Her skor, bileşenlerine ayrılabilmeli. Kullanıcı "bu yer neden yüksek puan aldı?" sorusunun cevabını görebilmeli.
2. **Kaynak şeffaflığı:** Her bileşen, hangi NASA verisinden geldiğiyle birlikte gösterilmeli.
3. **Görev türü esnekliği:** Kullanıcı görev türünü (jeoloji eğitimi, ISRU testi, gezgin testi, yaşam algılama, üs operasyonları) seçtiğinde ağırlıklar değişmeli.

### 13.2 Ay üssü profili

Ay üssü profilini, Bölüm 3.7'deki tabloya dayanarak şu Dünya ölçütlerine çeviriyoruz:

| Ölçüt | Ay'daki karşılığı | Dünya'daki ölçümü | NASA verisi |
|---|---|---|---|
| **K1. Kutup aydınlanması** | Neredeyse sürekli güneş alan sırtlar | Enlem; yaz gündönümündeki gün uzunluğu; güneşin ufka yakın açısı | Hesaplanır (enlemden) |
| **K2. Kalıcı soğuk** | Kalıcı gölgeli soğuk tuzaklar | Yıllık ortalama yüzey sıcaklığı; yılda donma günü sayısı | MODIS LST, MERRA-2 |
| **K3. Buz varlığı** | PSR'lerde su buzu | Kalıcı kar/buz örtüsü; buzullara veya donmuş zemine yakınlık | MODIS kar/buz, ICESat-2 |
| **K4. Sırt–krater topografyası** | Shackleton kenarı ve bağlantı sırtı | Yerel kabartı; sırt ve çukur yakınlığı; eğim dağılımı | SRTM/NASADEM, ASTER GDEM |
| **K5. Engebeli ama inilebilir arazi** | Engebeli kutup arazisi, düz iniş alanları | Pürüzlülük; düşük eğimli alanların oranı | SRTM/NASADEM, ASTER GDEM |
| **K6. Bitkisizlik** | Bitkisiz yüzey | NDVI | Landsat |
| **K7. Yalıtılmışlık** | Altyapısız ortam | Gece ışığı yoğunluğu | Black Marble |

**K1 ölçütü hakkında not:** Ay'ın kutup aydınlanmasının Dünya'da birebir karşılığı yok. Dünya'nın ekseni yaklaşık 23,4° eğik olduğu için kutup bölgelerinde yaz aylarında güneş batmıyor, kışın ise hiç doğmuyor. Bu, Ay'daki "bazı yerler sürekli aydınlık, bazı yerler sürekli karanlık" durumundan farklı. Ancak NASA'nın Haughton raporuna göre Haughton'un yaz koşulları, Shackleton'un sürekli gün ışığı alan kenarlarına benzetilebiliyor. Bu yüzden K1'i "yazın uzun süre batmayan ve ufka yakın açıyla gelen güneş" olarak tanımlıyoruz.

### 13.3 Mars profili

Mars profilini, Bölüm 6'daki hedeflere dayanarak şu ölçütlere çeviriyoruz:

| Ölçüt | Mars'taki karşılığı | Dünya'daki ölçümü | NASA verisi |
|---|---|---|---|
| **M1. Kuraklık** | Aşırı kuru yüzey | Yıllık yağış; nem | GPM IMERG, MERRA-2 |
| **M2. Mineral benzerliği** | Kil, sülfat, karbonat, demir oksit | EMIT mineral sınıfları ve bant derinlikleri | EMIT (Dünya), CRISM (Mars) |
| **M3. Topografya benzerliği** | Krater, delta, kanyon, düzlük | Eğim, kabartı, pürüzlülük dağılımları | SRTM/NASADEM (Dünya), MOLA (Mars) |
| **M4. Sıcaklık aralığı** | Büyük günlük sıcaklık farkı | Gece-gündüz sıcaklık farkı | MODIS LST |
| **M5. Bitkisizlik** | Bitkisiz yüzey | NDVI | Landsat |
| **M6. Soğukluk (isteğe bağlı)** | Soğuk ortam (özellikle buz hedefi için) | Yıllık ortalama sıcaklık | MODIS LST, MERRA-2 |
| **M7. Yeraltı buzu (isteğe bağlı)** | Arcadia Planitia gibi buz zengini bölgeler | Donmuş zemin, kar ve buz örtüsü | MODIS kar/buz |

Jezero hedefi seçilirse M2 (özellikle karbonat ve kil) ve M3 (delta biçimi) ağırlıklı olacak. Arcadia Planitia hedefi seçilirse M6 ve M7 ağırlıklı olacak.

### 13.4 Skor hesaplama

Her ölçüt için şu adımlar izlenecek:

1. **Normalleştirme:** Her Dünya değişkeni 0–1 aralığına çevrilecek. Uç değerlerin etkisini azaltmak için yüzdelik tabanlı normalleştirme (örneğin %2 ile %98 arası) kullanılacak.
2. **Hedef değer:** Her ölçüt için hedef profilden bir "ideal değer" veya "ideal aralık" tanımlanacak. Bazı ölçütler doğrudan karşılaştırılabilir (eğim, kabartı). Bazıları ise yön belirtir (kuraklık için "ne kadar kuru o kadar iyi", soğukluk için "ne kadar soğuk o kadar iyi").
3. **Ölçüt skoru:** Doğrudan karşılaştırılabilir ölçütler için hedefe olan uzaklığa göre bir benzerlik fonksiyonu kullanılacak. Örneğin Gauss biçimli bir fonksiyon: skor = exp(−(x − hedef)² / (2σ²)). Burada σ, ölçütün ne kadar hoşgörülü olacağını belirliyor. Yön belirten ölçütler için doğrudan normalleştirilmiş değer kullanılacak.
4. **Ağırlıklı toplam:** Ölçüt skorları, görev türüne göre belirlenen ağırlıklarla toplanacak. Ağırlıkların toplamı 1 olacak.
5. **Eşik kuralları:** Bazı ölçütler "olmazsa olmaz" kabul edilebilir. Örneğin Ay üssü profili için K6 (bitkisizlik) belirli bir eşiğin altındaysa, diğer ölçütler ne kadar yüksek olursa olsun toplam skor sınırlanabilir. Bu, ormanlık veya tarım alanlarının yanlışlıkla üst sıralara çıkmasını önler.

### 13.5 Görev türüne göre ağırlıklar

NASA'nın üç analog türü (Bölüm 7.2) ve Moon Base ihtiyaçları (Bölüm 3.7) temel alınarak beş görev türü tanımlıyoruz. Aşağıdaki ağırlıklar başlangıç önerisidir. Doğrulama sonuçlarına göre ayarlanacak.

**Ay üssü profili için:**

| Görev türü | K1 Aydınlanma | K2 Soğuk | K3 Buz | K4 Sırt–krater | K5 Arazi | K6 Bitkisizlik | K7 Yalıtılmışlık |
|---|---|---|---|---|---|---|---|
| Üs operasyonları (görev analoğu) | 0,15 | 0,15 | 0,15 | 0,15 | 0,10 | 0,10 | 0,20 |
| Kaynak arama (ISRU, buz) | 0,10 | 0,20 | 0,30 | 0,10 | 0,10 | 0,10 | 0,10 |
| Gezgin ve konvoy testi | 0,10 | 0,10 | 0,10 | 0,20 | 0,25 | 0,15 | 0,10 |
| Enerji planlama (güneş) | 0,35 | 0,10 | 0,10 | 0,20 | 0,05 | 0,10 | 0,10 |
| Jeoloji eğitimi | 0,05 | 0,05 | 0,05 | 0,30 | 0,20 | 0,30 | 0,05 |

**Mars profili için:**

| Görev türü | M1 Kuraklık | M2 Mineral | M3 Topografya | M4 Sıcaklık aralığı | M5 Bitkisizlik | M6 Soğuk | M7 Buz |
|---|---|---|---|---|---|---|---|
| Yaşam algılama (astrobiyoloji) | 0,30 | 0,30 | 0,10 | 0,05 | 0,15 | 0,05 | 0,05 |
| Gezgin testi | 0,15 | 0,05 | 0,40 | 0,05 | 0,25 | 0,05 | 0,05 |
| İnsanlı üs (buz) | 0,10 | 0,05 | 0,15 | 0,10 | 0,15 | 0,20 | 0,25 |
| Jeoloji eğitimi | 0,15 | 0,30 | 0,30 | 0,05 | 0,15 | 0,00 | 0,05 |

### 13.6 Ölçek uyumu

Ay ve Mars verileri ile Dünya verileri farklı çözünürlüklerde. LOLA kutuplarda metrelerce çözünürlük sunarken MOLA yüzlerce metre, MERRA-2 ise onlarca kilometre çözünürlükte. Bu fark iki şekilde ele alınacak:

1. **Analiz ızgarası:** Küresel tarama için kaba bir ızgara (örneğin 0,1° veya 0,25°) kullanılacak. Bu, iklim verilerinin çözünürlüğüyle uyumlu.
2. **Yerel inceleme:** Kaba ızgarada üst sıralara çıkan aday bölgeler, ince çözünürlüklü verilerle (SRTM 30 m, EMIT 60 m, Landsat 30 m) ayrıca incelenecek.

Topografya karşılaştırmasında hedef ile aday aynı ölçekte ölçülmeli. Örneğin LOLA'dan 100 m ölçeğinde hesaplanan bir eğim dağılımı, SRTM'den yine 100 m ölçeğine indirgenmiş bir eğim dağılımıyla karşılaştırılmalı. Aksi hâlde eğim değerleri yanıltıcı olur.

### 13.7 Belirsizlik

Her skor bir belirsizlik bilgisiyle birlikte verilecek. Belirsizliğin kaynakları:

- **Veri kapsamı:** Bir hücrede bazı ölçütler için veri yoksa (örneğin EMIT kutuplarda yok), skor eksik ölçütlerle hesaplanacak ve bu durum işaretlenecek.
- **Ağırlık duyarlılığı:** Ağırlıklar ±%20 değiştirildiğinde bir adayın sıralaması çok değişiyorsa, o aday "duyarlı" olarak işaretlenecek.
- **Kısmi analog uyarısı:** Hiçbir skor "bu yer Ay'ın aynısıdır" anlamına gelmeyecek. Arayüzde her zaman "hangi bakımdan benzer, hangi bakımdan farklı" bilgisi gösterilecek.

### 13.8 "Yeni aday" tanımı

Görev, bilinen analogların listelenmesini değil, **yeni** analogların bulunmasını istiyor. Bu yüzden "yeni"liği ölçmek için bir kural gerekiyor:

- Doğrulama setindeki bilinen analogların (Bölüm 14.1) her birine olan uzaklık hesaplanacak.
- Bilinen bir analoga belirli bir uzaklıktan (örneğin 300 km) daha yakın olan adaylar "bilinen analog bölgesi" olarak işaretlenecek.
- Yüksek skorlu ve bilinen analoglardan uzak olan adaylar "yeni aday" olarak öne çıkarılacak.

---

## 14. Doğrulama planı

### 14.1 Doğrulama seti

Modelin doğru çalışıp çalışmadığını anlamak için, NASA'nın zaten analog olarak kullandığı yerlerden oluşan bir "bilinen pozitifler" seti ve analog olmadığı açık olan yerlerden oluşan bir "negatif kontroller" seti kullanılacak.

**Ay üssü profili için bilinen pozitifler:**
- Haughton Krateri (NASA: Ay analog sahası, Shackleton–Malapert simülasyonu)
- McMurdo Kuru Vadileri (NASA: en soğuk ve kuru ortamlar, buzla çimentolanmış zemin)
- Askja çevresi (NASA: yeraltı buzu araştırması, Apollo ve Artemis eğitimi). Bu, kısmi bir pozitif.
- Mauna Kea (NASA: Ay kutup görevi simülasyonu). Bu da kısmi bir pozitif; kutup ortamı olmadığı için orta düzey skor beklenir.

**Mars profili için bilinen pozitifler:**
- Atacama hiper-kurak çekirdeği (NASA: ARADS, Life in the Atacama)
- Salda Gölü (NASA: Jezero analoğu)
- Death Valley (NASA: Mars 2020 çalışması)
- Pilot Valley (NASA: perklorat içeren tuzlar)
- Haughton (NASA: Mars görev analoğu)
- McMurdo Kuru Vadileri (NASA: eski Mars analoğu)

**Negatif kontroller (her iki profil için):**
- Yoğun tropikal ormanlar (Landsat NDVI'si çok yüksek bölgeler)
- Yoğun tarım alanları
- Büyük kentler (Black Marble'da çok parlak bölgeler)

**Ekibin listesindeki yerlerin rolü:**
- Atacama, Askja ve Mauna Kea, NASA tarafından da kullanıldığı için pozitif sete giriyor.
- Wadi Rum, Kapadokya ve Bardenas Reales için NASA'nın analog kullanımı bulunamadığı için bu üç yer pozitif sete **alınmayacak**. Bunun yerine "test vakası" olarak kullanılacak. Model bunlara hangi skoru veriyor ve neden? Bu analiz, görsel benzerlik ile ölçülmüş benzerlik arasındaki farkı göstermek için sunumda kullanılabilir.

### 14.2 Başarı ölçütleri

1. **Sıralama testi:** Bilinen pozitifler, rastgele seçilmiş kara hücrelerinden daha yüksek skor almalı. Bu, ROC eğrisi altındaki alan (AUC) ile ölçülecek. AUC = 0,5 rastgele tahmine eşit, AUC = 1 kusursuz ayrım demek. Hedefimiz her iki profil için AUC'nin belirgin şekilde 0,5'in üstünde olması.
2. **Üst dilim testi:** Bilinen pozitiflerin ne kadarının Dünya karalarının en yüksek skorlu %10'luk diliminde yer aldığına bakılacak.
3. **Negatif kontrol testi:** Negatif kontrollerin hiçbiri üst %10'luk dilimde yer almamalı.
4. **Profil ayrımı testi:** Ay üssü pozitifleri Ay üssü profilinde, Mars pozitifleri Mars profilinde daha yüksek skor almalı. Örneğin Salda Gölü'nün Mars skoru Ay üssü skorundan belirgin şekilde yüksek olmalı.

### 14.3 Duyarlılık analizi

- **Ağırlık duyarlılığı:** Her ağırlık ±%20 değiştirilerek sıralamaların ne kadar değiştiğine bakılacak.
- **Ölçüt çıkarma testi:** Her ölçüt sırayla modelden çıkarılarak AUC'nin ne kadar düştüğü ölçülecek. Bu, hangi ölçütün en çok bilgi taşıdığını gösterecek.
- **Çözünürlük testi:** Analiz ızgarası 0,25° ile 0,1° arasında değiştirilerek sonuçların kararlılığı kontrol edilecek.

### 14.4 Dürüst raporlama

Doğrulama sonuçları zayıf çıkarsa bu sunumda gizlenmeyecek. Örneğin Ay üssü profili için bilinen pozitif sayısı az (yalnızca birkaç kutup analoğu). Bu yüzden AUC değeri istatistiksel olarak belirsiz olabilir. Bu durum açıkça belirtilecek ve "daha fazla NASA kutup analoğu ile doğrulama gerekiyor" şeklinde bir sonraki adım olarak sunulacak.

---

## 15. Uygulama ve yazılım mimarisi

### 15.1 Genel yapı

Proje dört katmandan oluşacak:

1. **Veri toplama katmanı:** NASA veri setlerinin indirilmesi ve kırpılması.
2. **İşleme katmanı:** Ölçütlerin hesaplanması, normalleştirme, ızgaraya aktarma.
3. **Puanlama katmanı:** Hedef profiller, ağırlıklar, skorlar, belirsizlik ve "yenilik" hesabı.
4. **Sunum katmanı:** Etkileşimli harita, aday listeleri, açıklamalar ve karşılaştırma görselleri.

### 15.2 Veri toplama

- **NASA Earthdata:** Dünya veri setleri (SRTM/NASADEM, ASTER GDEM, ICESat-2, HLSL30, EMIT, MODIS, MERRA-2, GPM) NASA Earthdata üzerinden erişilebilir. İndirme için ücretsiz bir Earthdata Login hesabı gerekiyor. Arama ise hesap olmadan da yapılabiliyor.
- **NASA Solar System Treks:** Moon Trek ve Mars Trek, Ay ve Mars için hazır harita katmanları (örneğin LOLA ve LROC mozaikleri, MOLA ve CTX mozaikleri) sunuyor. Bu katmanlar web harita servisleri olarak kullanılabiliyor. Bu, hackathon süresinde hedef bölgelerin hızlıca görselleştirilmesi için pratik bir yol.
- **NASA PDS:** LRO, MRO ve Artemis II'nin ham ve işlenmiş verileri PDS'te.
- **NASA GIBS:** Dünya için hazır görüntü katmanları (örneğin Blue Marble) NASA'nın GIBS servisinden alınabilir.

### 15.3 İşleme

İşleme Python ile yapılacak. Önerilen adımlar:

1. Her veri setini ortak bir küresel ızgaraya (örneğin 0,25°) yeniden örnekleme.
2. Her hücre için ölçüt değerlerini hesaplama (örneğin SRTM'den eğim ve kabartı, MODIS'ten yıllık ortalama sıcaklık, GPM'den yıllık yağış).
3. Eksik veri maskelerinin oluşturulması (örneğin SRTM'nin 60° kuzeyin üstünde olmaması, EMIT'in kutuplarda olmaması).
4. Hedef profillerin LRO ve Mars verilerinden çıkarılması. Hackathon süresi kısıtlı olduğu için hedef değerler başlangıçta NASA kaynaklarındaki yayımlanmış değerlerden ve Trek katmanlarından alınabilir, ardından ham veriyle iyileştirilebilir.

### 15.4 Puanlama

Puanlama modülü şu girdileri alacak:

- hedef profil (Ay üssü veya Mars; Mars için Jezero veya Arcadia),
- görev türü (Bölüm 13.5),
- isteğe bağlı kullanıcı ağırlıkları.

Çıktıları:

- her hücre için toplam skor,
- her hücre için ölçüt bazında skor dökümü,
- her hücre için hangi NASA verisinin kullanıldığı bilgisi,
- belirsizlik ve "yenilik" işaretleri.

### 15.5 Sunum arayüzü

Arayüzde şunlar olmalı:

1. **Küresel ısı haritası:** Seçilen profil ve görev türüne göre Dünya karalarının skorları.
2. **Aday listesi:** En yüksek skorlu ilk 10–20 aday, "bilinen" veya "yeni" etiketiyle.
3. **Aday kartı:** Her aday için:
   - ölçüt bazında skor dökümü (örneğin çubuk grafik),
   - her ölçütün hangi NASA verisinden geldiği,
   - hedefe göre "benzer olduğu" ve "farklı olduğu" yönler,
   - en yakın bilinen NASA analoğu ve ona olan uzaklık.
4. **Yan yana karşılaştırma:** Aday bölgenin Landsat görüntüsü ile hedefin Trek görüntüsü (Ay için LROC, Mars için CTX) yan yana. Mümkünse Artemis II'den bir fotoğraf.
5. **Doğrulama paneli:** Bilinen pozitiflerin ve negatif kontrollerin skorları, AUC değeri.

---

## 16. Hackathon zaman planı

NASA Space Apps Challenge 2026, 14–15 Kasım 2026 tarihlerinde yapılıyor. Bu rapor 14 Kasım sabahı hazırlandığı için kalan süre yaklaşık bir buçuk gün. Aşağıdaki plan bu süreye göre hazırlandı.

### 16.1 Birinci gün (14 Kasım)

| Saat | İş | Çıktı |
|---|---|---|
| Öğleden önce | Hedef profillerin kesinleştirilmesi (Shackleton Connecting Ridge; Jezero ve isteğe bağlı Arcadia) | Hedef değer tablosu |
| Öğleden önce | Veri setlerinin indirilmesi (önce kaba çözünürlüklü küresel ürünler) | Ham veri klasörü |
| Öğleden sonra | Ortak ızgara ve ölçütlerin hesaplanması | Ölçüt katmanları |
| Öğleden sonra | Puanlama modülünün ilk sürümü | İlk skor haritası |
| Akşam | Doğrulama testleri (AUC, üst dilim) | Doğrulama sonuçları |
| Gece | Ağırlıkların ayarlanması, duyarlılık analizi | İyileştirilmiş skorlar |

### 16.2 İkinci gün (15 Kasım)

| Saat | İş | Çıktı |
|---|---|---|
| Sabah | Yeni adayların belirlenmesi ve ince çözünürlüklü incelenmesi | Aday kartları |
| Öğle | Arayüzün tamamlanması | Çalışan demo |
| Öğleden sonra | Sunum ve proje sayfası metninin hazırlanması | Sunum, metin |
| Akşam | Son kontroller ve gönderim | Gönderilmiş proje |

### 16.3 Zaman yetmezse öncelik sırası

1. Ay üssü profili ve doğrulaması (görevin adındaki ana hedef).
2. Mars profili (yalnızca Jezero) ve Salda ile doğrulama.
3. Arayüzde ölçüt dökümü ve veri kaynağı gösterimi.
4. Arcadia Planitia profili.
5. Artemis II görsel karşılaştırması.

---

## 17. Sunum ve anlatı stratejisi

### 17.1 Ana mesaj

Sunumun ana mesajı tek cümleyle şu olabilir: **"NASA'nın Ay üssü için seçtiği yere ve Mars hedeflerine benzeyen yerleri, yalnızca NASA verileriyle, açıklanabilir ve doğrulanmış bir şekilde Dünya üzerinde bulduk."**

### 17.2 Anlatı akışı

1. **Sorun:** NASA, Moon Base için Shackleton Connecting Ridge'i seçti. Astronotlar ve robotlar bu ortamı Dünya'da prova etmek zorunda. Ama bugünkü analogların çoğu "Ay'a benzeyen" yerler, "Ay üssüne benzeyen" yerler değil.
2. **Kanıt:** Ekibin başlangıç listesindeki altı yerin hiçbiri kutup ve buz ölçütlerini karşılamıyor. NASA'nın kendi kutup analoğu Haughton bu boşluğu dolduruyor.
3. **Yöntem:** Hedef profiller NASA'nın Ay ve Mars verilerinden çıkarıldı. Dünya, NASA'nın Dünya verileriyle puanlandı.
4. **Doğrulama:** Model, NASA'nın zaten kullandığı analogları (Haughton, Atacama, Salda vb.) üst sıralara koyuyor.
5. **Yeni adaylar:** Model, bilinen analoglardan uzakta yeni adaylar öneriyor. Her biri için neden benzediği ve nerede farklı olduğu gösteriliyor.
6. **Türkiye bağlantısı:** NASA'nın Jezero için kullandığı Salda Gölü, modelimizin Mars doğrulamasında başarılı bir örnek.

### 17.3 Jüriye gösterilecek güçlü noktalar

- **Güncellik:** Moon Base programının en son kararları (Mayıs ve 7 Kasım 2026) ve Artemis II verileri (Ekim 2026) kullanıldı.
- **Veri disiplini:** Bütün veriler NASA'ya ait. Kaynak politikası açıkça belirtildi.
- **Açıklanabilirlik:** Her skor, bileşenlerine ve veri kaynaklarına ayrılabiliyor.
- **Bilimsel dürüstlük:** Kısmi analog kavramı ve sınırlılıklar açıkça gösteriliyor.
- **Görev türü esnekliği:** Aynı yer, farklı görev türleri için farklı skorlar alabiliyor. Bu, NASA'nın üç analog türü sınıflandırmasıyla uyumlu.

### 17.4 Kaçınılacak şeyler

- Uygunluk notlarını (●●●) veriyle hesaplanmış gibi sunmak.
- "Bu yer Ay'ın aynısı" gibi abartılı ifadeler kullanmak.
- NASA'nın analog olarak kullanmadığı bir yeri (örneğin Kapadokya) "NASA'nın analoğu" gibi sunmak.
- Başka takımların çalışmalarına atıf yapmak veya onlarla karşılaştırma yapmak.

---

## 18. Riskler, sınırlılıklar ve açık sorular

### 18.1 Veri riskleri

| Risk | Etkisi | Önlem |
|---|---|---|
| SRTM'nin 60° kuzeyin üstünü kapsamaması | Kutup analogları için topografya eksik | ASTER GDEM ve ICESat-2 kullanmak |
| ICESat-2 ATL14'ün yalnızca kara buzu bölgelerini kapsaması | Buzsuz kutup çölleri için yükseklik eksik | ASTER GDEM ile tamamlamak |
| EMIT'in kutupları kapsamaması | Kutup analogları için mineral bilgisi yok | Ay üssü profilinde mineral ölçütü kullanmamak |
| Earthdata Login gerekliliği | İndirme gecikmesi | Hesapları ilk saatte açmak |
| Büyük veri boyutları | İşleme süresi uzar | Önce kaba çözünürlüklü küresel ürünlerle başlamak |

### 18.2 Yöntem riskleri

- **Az sayıda kutup pozitifi:** Ay üssü profili için bilinen pozitif sayısı az. Bu, doğrulama sonuçlarını istatistiksel olarak zayıflatabilir.
- **Ağırlıkların öznelliği:** Başlangıç ağırlıkları ekibin değerlendirmesine dayanıyor. Duyarlılık analizi bu riski azaltır ama ortadan kaldırmaz.
- **Ölçek uyumsuzluğu:** Ay ve Mars verileri ile Dünya verileri arasındaki çözünürlük farkı, topografya karşılaştırmasını yanıltabilir.

### 18.3 Fiziksel sınırlılıklar

Dünya'da hiçbir yer şunları taklit edemiyor:

- Ay'ın neredeyse sıfır atmosferini ve vakumunu,
- Ay'ın kalıcı gölgeli bölgelerindeki yaklaşık 33 Kelvin'lik sıcaklığı,
- Ay ve Mars yüzeyindeki uzay radyasyonunu,
- Ay'ın düşük yer çekimini,
- Mars'ın ince karbondioksit atmosferini.

Bu sınırlılıklar sunumda açıkça belirtilmeli. Modelimiz yalnızca Dünya'da ölçülebilen ve uydu verisiyle gözlenebilen özellikleri karşılaştırıyor.

### 18.4 Açık sorular

1. Artemis II görüntüleri Shackleton Connecting Ridge'i kapsıyor mu? (PDS kullanıcı kılavuzundan kontrol edilmeli.)
2. Mars hedefi olarak yalnızca Jezero mu kullanılmalı, yoksa Arcadia Planitia da eklenmeli mi?
3. "Yeraltı habitatı" (mağara) ölçütü eklenmeli mi? Görev metni mağaraları açıkça andığı için bu düşünülmeli.
4. Projenin gönderim dili ne olmalı? Global değerlendirmeye gidecekse İngilizce metin gerekebilir. Bu, resmi gönderim kurallarından kontrol edilmeli.

---

## 19. Önceki sürümlerde yapılan düzeltmeler

Bu rapor, süreç boyunca üretilen belgelerin birleşimi. Önceki sürümlerde yapılan ve bu raporda korunan düzeltmeler şunlar:

**Görevin tanımıyla ilgili:**
- Görevin Ay'da üs yeri seçmek değil, Dünya'da analog bulmak olduğu netleştirildi.

**Ekibin dosyasıyla ilgili:**
1. **Kapadokya:** "Krater benzeri oyuklar" ifadesinin yanıltıcı olduğu belirtildi. NASA'nın bu yeri analog olarak kullandığına dair kayıt bulunamadığı eklendi.
2. **Wadi Rum:** "Ay Vadisi" adının doğru olduğu doğrulandı. NASA'nın dağları "bazalt" değil, "granit ve kumtaşı" olarak tanımladığı belirtildi.
3. **Atacama:** Turistik "Ay Vadisi" ile NASA test sahasının ayrı yerler olduğu belirtildi. NASA kaynaklarında Atacama'da Ay araçlarının test edildiğine dair kayıt bulunamadığı eklendi.
4. **Askja:** İfadenin doğru olduğu doğrulandı. Artemis II eğitimi ve yeraltı buzu araştırması eklendi.
5. **Mauna Kea:** "Ay kraterlerini birebir simüle eder" ifadesinin abartılı olduğu, asıl değerin regolit benzeri malzeme ve ISRU testlerinden geldiği belirtildi.
6. **Bardenas Reales:** NASA'nın bu yeri analog olarak kullandığına dair kayıt bulunamadığı belirtildi. "Tebeşirli" ifadesi için NASA kaynaklarında destek bulunamadığı eklendi.

**Kaynak politikasıyla ilgili:**
- Bütün NASA dışı kaynaklar (başka ajansların veri setleri, akademik makaleler, ansiklopedi ve haber siteleri) çıkarıldı.
- Başka takımlara dair her türlü bilgi çıkarıldı.
- NASA dışı yükseklik modelleri yerine ICESat-2 ve ASTER GDEM kullanıldı.
- HLS ürününün yalnızca Landsat kısmı (HLSL30) kullanıldı.

**Bilgi düzeltmeleri:**
- Haughton Krateri'nin yaşı, NASA kaynağına göre yaklaşık 38 milyon yıl olarak düzeltildi.

**Yeni eklenenler:**
- Haughton Krateri (Ay üssü için eksik halka)
- Salda Gölü (Türkiye'den NASA onaylı Mars analoğu)
- McMurdo Kuru Vadileri, Death Valley, Kilauea, Medicine Lake, Pilot Valley, Verde Valley, Katmai ve Mojave (NASA'nın kullandığı ek analoglar)
- Moon Base aşamaları ve 7 Kasım 2026 duyuruları
- LRO aletlerinin ayrıntılı tanımları
- NASA'nın insanlı Mars iniş bölgesi ölçütleri
- Puanlama modeli, doğrulama planı, yazılım mimarisi ve zaman planı

---

## 20. Sözlük

- **Analog (gezegen analoğu):** Dünya'da, başka bir gök cismindeki koşullara bazı bakımlardan benzeyen yer.
- **Astrobiyoloji analoğu:** Yaşamın sınırlarını incelemeye ve yaşam algılama araçlarını denemeye uygun analog.
- **ATL14:** ICESat-2'nin Antarktika ve Arktik kara buzu bölgeleri için ürettiği 100 m çözünürlüklü yükseklik modeli.
- **AUC (ROC eğrisi altındaki alan):** Bir modelin pozitif ve negatif örnekleri ne kadar iyi ayırdığını gösteren ölçü. 0,5 rastgele, 1 kusursuz.
- **CLPS (Commercial Lunar Payload Services):** NASA'nın Ay'a ticari yük taşıma programı.
- **CRISM:** MRO'daki, Mars yüzeyinin mineral bileşimini haritalayan görüntüleme spektrometresi.
- **Diviner (DLRE):** LRO'daki, Ay yüzeyinin sıcaklığını ölçen radyometre.
- **EMIT:** Uluslararası Uzay İstasyonu'ndaki, Dünya'nın kurak bölgelerinin mineral bileşimini haritalayan görüntüleme spektrometresi.
- **Görev analoğu:** İnsanlı ve robotik operasyonların, lojistiğin ve yalıtılmışlığın prova edildiği analog.
- **ISRU (yerinde kaynak kullanımı):** Gidilen yerdeki kaynakları (örneğin buz, regolit) kullanarak su, oksijen veya yakıt üretme.
- **Jeolojik analog:** Başka bir gök cismindeki jeolojik süreçlere veya yapılara benzeyen analog.
- **Keşif Bölgesi (Exploration Zone):** NASA'nın insanlı Mars görevleri için tanımladığı, iniş yerinin yaklaşık 100 km çevresindeki ilgi bölgelerinin toplamı.
- **LAMP:** LRO'daki, Ay yüzeyini uzak morötesi ışıkta haritalayan alet.
- **LEND:** LRO'daki, hidrojen dağılımını haritalayan nötron dedektörü.
- **LOLA:** LRO'daki, Ay'ın topografyasını ölçen lazer altimetre.
- **LRO (Lunar Reconnaissance Orbiter):** NASA'nın Ay yörüngesindeki keşif uydusu.
- **LROC:** LRO'nun kamera sistemi (iki dar açılı ve bir geniş açılı kamera).
- **LTV (Lunar Terrain Vehicle):** Ay arazi aracı.
- **Mikrobiyalit:** Mikropların yardımıyla oluşan kaya yapısı.
- **Mini-RF:** LRO'daki, yeraltı buzu arayan radar.
- **MOLA:** Mars Global Surveyor'daki, Mars'ın topografyasını ölçen lazer altimetre.
- **Moon Base:** NASA'nın Ay'ın Güney Kutbu'nda kurmayı planladığı kalıcı karakol.
- **NDVI:** Bitki örtüsü yoğunluğunu gösteren indeks.
- **PDS (Planetary Data System):** NASA'nın gezegen görevleri için kamu arşivi.
- **PROMISE:** NASA'nın Ay'ın Güney Kutbu için geliştirdiği nükleer enerjili gezgin.
- **PSR (kalıcı gölgeli bölge):** Ay'ın kutuplarında güneş ışığı hiç almayan bölgeler.
- **Regolit:** Ay ve Mars yüzeyini örten gevşek, ince taneli malzeme.
- **Shackleton Connecting Ridge:** Ay'ın Güney Kutbu'nda, Moon Base I görevinin hedeflediği sırt.
- **Soğuk tuzak:** Uçucu maddeleri uzun süre tutabilecek kadar soğuk bölge.
- **SRTM / NASADEM:** NASA'nın 60° K – 56° G arasındaki karalar için yaklaşık 30 m çözünürlüklü yükseklik modelleri.
- **SWIM (Subsurface Water Ice Mapping):** NASA'nın Mars'taki yeraltı buzunu haritalama projesi.
- **VIPER:** NASA'nın Ay'ın Güney Kutbu'nda su buzunu haritalayacak gezgini.

---

## 21. Kaynaklar (yalnızca NASA)

### Görev ve Moon Base programı
- NASA Space Apps Challenge 2026, görev sayfası: https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/
- NASA, Moon Base ana sayfası: https://www.nasa.gov/moonbase/
- NASA, Moon Base hakkında: https://www.nasa.gov/reference/moonbase-about/
- NASA, Moon Base aşamaları: https://www.nasa.gov/moonbase-phases/
- NASA, Moon Base medya kaynakları: https://www.nasa.gov/moonbase-media-resources/
- NASA, Moon Base güncellemesi (Mayıs 2026): https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/
- NASA, Moon Base bilim ödülleri (Haziran 2026): https://www.nasa.gov/news-release/nasa-awards-more-moon-base-science-previews-new-opportunities/
- NASA, Moon Base ulaşım, teknoloji ve bilim projeleri (7 Kasım 2026): https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/
- NASA JPL, aynı duyuru: https://www.jpl.nasa.gov/news/nasa-awards-moon-base-transportation-technology-science-projects/
- NASA, Artemis III iniş bölgeleri güncellemesi: https://www.nasa.gov/news-release/nasa-provides-update-on-artemis-iii-moon-landing-regions/

### Yeni veriler
- NASA, Artemis II Ay bilimi verileri (Ekim 2026): https://www.nasa.gov/blogs/missions/2026/10/07/nasa-releases-artemis-ii-lunar-science-data-images/

### LRO ve Ay Güney Kutbu
- NASA, LRO uzay aracı ve aletleri: https://science.nasa.gov/mission/lro/spacecraft-and-instruments/
- NASA, LRO genel tanıtım makalesi: https://science.nasa.gov/wp-content/uploads/2024/01/lro-space-science-paper.pdf
- NASA, LAMP teknik özeti: https://science.nasa.gov/wp-content/uploads/2024/01/keller51906.pdf
- NASA NSSDCA, LRO: https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2009-031A
- NASA, Moon to Mars Ay Yüzeyi Veri Kitabı: https://ntrs.nasa.gov/api/citations/20250002845/downloads/M2M-30044%20Lunar%20Surface%20Data%20Book%20Baseline_Final.pdf
- NASA, LRO'nun ilk ölçümleri (2009): https://www3.nasa.gov/home/hqnews/2009/sep/HQ_09-215_LRO_First_Light.html
- NASA Astrobiyoloji, LRO: https://astrobiology.nasa.gov/missions/lro/

### Mars
- NASA, Mars Kampanyası ve Keşif Bölgeleri: https://ntrs.nasa.gov/api/citations/20160006342/downloads/20160006342.pdf
- NASA, Mars'ta su buzu hazine haritası: https://www.nasa.gov/solar-system/nasas-treasure-map-for-water-ice-on-mars/
- NASA, Mars'ta astronotlar nereye inmeli: https://www.nasa.gov/centers-and-facilities/jpl/where-should-future-astronauts-land-on-mars-follow-the-water/
- NASA, SWIM yeraltı buzu haritası: https://science.nasa.gov/resource/swim-map-shows-subsurface-water-ice-on-mars/
- NASA, Mars'ta buz haritası: https://www.nasa.gov/solar-system/planets/mars/nasa-is-locating-ice-on-mars-with-this-new-map/
- NASA, İnsanlı Mars iniş yeri çalıştayı (2015): https://www.nasa.gov/wp-content/uploads/2015/06/mars-c-abstracts_in_order_of_presentation10242015_0.pdf

### Analoglar genel
- NASA, Gezegen Analogları Hakkında 10 Şey: https://science.nasa.gov/solar-system/planetary-analogs/10-things-to-know-about-planetary-analogs/
- NASA, Gezegen Analog Gezgini: https://science.nasa.gov/solar-system/analog-explorer/
- NASA Astrobiyoloji, saha listesi: https://astrobiology.nasa.gov/research-locations/
- NASA, analog görevler bilgi notu: https://www.nasa.gov/wp-content/uploads/2015/06/541196main_analogfactsheet.pdf

### Kapadokya
- NASA Earth Observatory, Göreme Milli Parkı: https://earthobservatory.nasa.gov/images/38876/goreme-national-park-turkey

### Wadi Rum
- NASA Earth Observatory, Movie Mars on Earth: https://science.nasa.gov/earth/earth-observatory/movie-mars-on-earth-148764/
- NASA Earth Observatory, Wadi Rum (2001): https://science.nasa.gov/earth/earth-observatory/wadi-rum-jordan-49945/

### Atacama
- NASA Astrobiyoloji, ARADS: https://astrobiology.nasa.gov/news/nasa-tests-life-detection-drill-in-the-atacama-desert/
- NASA, Tire Tracks on "Mars": https://www.nasa.gov/image-article/tire-tracks-mars-atacama-rover-astrobiology-drilling-studies/
- NASA Astrobiyoloji Enstitüsü, Dünya'nın en kurak yeri: https://astrobiology.nasa.gov/nai/articles/2002/4/24/the-driest-place-on-earth/index.html
- NASA, Life in the Atacama (Zoë): https://www.nasa.gov/general/drilling-our-way-to-life-on-mars-rover-mounted-drill-autonomously-explores-subsurface-life-in-the-atacama-desert-chile/
- NASA Astrobiyoloji, Atacama'da otonom analiz: https://astrobiology.nasa.gov/news/autonomous-analysis-in-the-atacama/
- NASA JPL, Atacama'da yaşam algılama: https://www.jpl.nasa.gov/news/detecting-life-in-the-ultra-dry-atacama-desert/

### Askja ve İzlanda
- NASA, Apollo astronot jeoloji eğitimi kayıtları: https://www.nasa.gov/wp-content/uploads/static/history/alsj/AstronautGeologyTraining.pdf
- NASA, Apollo 13 Avrupa turu: https://www.nasa.gov/history/50-years-ago-apollo-13-aquarius-european-goodwill-tour/
- NASA, Where No Man Has Gone Before, Ek 7: https://www.hq.nasa.gov/office/pao/History/SP-4214/app7.html
- NASA, Artemis II mürettebatı İzlanda'da: https://science.nasa.gov/missions/artemis/nasas-artemis-ii-crew-uses-iceland-terrain-for-lunar-training/
- NASA ESPO, Askja ASTER haritalaması: https://espo.nasa.gov/atom/content/Remote_sensing_and_geologic_mapping_of_glaciovolcanic_deposits_in_the_region_surrounding
- NASA, Apollo astronotlarının bilim eğitimi tarihi: https://ntrs.nasa.gov/api/citations/20190026783/downloads/20190026783.pdf

### Mauna Kea
- NASA NTRS, Mauna Kea ISRU testleri 2010 ve 2012: https://ntrs.nasa.gov/citations/20140008708
- NASA NTRS, PISCES (2007): https://ntrs.nasa.gov/api/citations/20070037451/downloads/20070037451.pdf
- NASA analog görevler, ISRU 2012 (arşivlenmiş nasa.gov sayfası): https://webarchive.library.unt.edu/web/20130221205815/http://www.nasa.gov/exploration/analogs/isru/index.html

### Bardenas Reales
- NASA APOD, Bardenas Reales: https://science.nasa.gov/image-article/apod-2013-september-2-milky-way-over-spains-bardenas-reales/

### Haughton
- NASA/TM-2011-216157: https://ntrs.nasa.gov/api/citations/20110011887/downloads/20110011887.pdf
- NASA analog testleri blogu, HMP-2010: https://blogs.nasa.gov/analogsfieldtesting/2010/08/03/post_1280841076434/
- NASA NTRS, Haughton yaşı ve Mars iklimi: https://ntrs.nasa.gov/citations/20050170975
- NASA NTRS, Devon Adası'nda Mars benzeri küçük vadiler: https://ntrs.nasa.gov/api/citations/20000092052/downloads/20000092052.pdf
- NASA NTRS, Haughton-Mars Project 2005 raporu: https://ntrs.nasa.gov/api/citations/20060013129/downloads/20060013129.pdf

### Salda Gölü
- NASA Earth Matters, Türkiye'deki bir göl Mars hakkında ne söyler: https://science.nasa.gov/blogs/earth-matters/2021/02/17/what-a-lake-in-turkey-can-tell-us-about-mars/
- NASA Earth Observatory, Jez like Mars: https://science.nasa.gov/earth/earth-observatory/jez-like-mars-147041/
- NASA, Salda Gölü kıyısı: https://science.nasa.gov/photojournal/lake-salda-beach/
- NASA JPL, Salda Gölü kayaları: https://www.jpl.nasa.gov/images/pia24374-lake-salda-rocks/

### Diğer NASA analogları
- NASA Earth Observatory, Ay oyunu (Katmai): https://science.nasa.gov/earth/earth-observatory/playing-the-moon-game/

### Dünya veri setleri
- NASA Earthdata, SRTMGL1: https://www.earthdata.nasa.gov/data/catalog/lpcloud-srtmgl1-003
- NASA Earthdata, ICESat-2 ATL14: https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-atl14-005
- NASA ICESat-2, ATL14/ATL15 algoritma belgesi: https://icesat-2.gsfc.nasa.gov/sites/default/files/page_files/ICESat2_ATL14_ATL15_ATBD_r005.pdf
- NASA Earthdata, HLSL30: https://www.earthdata.nasa.gov/data/catalog/lpcloud-hlsl30-2.0
- NASA Earthdata, EMIT L2B mineral ürünü: https://www.earthdata.nasa.gov/data/catalog/lpcloud-emitl2bmin-002
- NASA Earthdata, EMIT tanıtımı: https://www.earthdata.nasa.gov/news/feature-articles/meet-emit-newest-imaging-spectrometer
- NASA JPL, EMIT: https://earth.jpl.nasa.gov/emit/
- NASA Earth Observatory, Antakya'da karanlık geceler (Black Marble): https://science.nasa.gov/earth/earth-observatory/dark-nights-in-antakya-151029/
- NASA Solar System Treks (Moon Trek, Mars Trek): https://trek.nasa.gov

---

## 22. Ekler

### Ek A: Örnek aday kartı (Haughton Krateri)

Bu ek, arayüzde her aday için gösterilecek "aday kartı"nın nasıl görüneceğini, NASA'nın bilinen bir analoğu olan Haughton Krateri üzerinden örnekliyor. Aşağıdaki değerler model çalıştırıldığında hesaplanacak. Burada yalnızca kartın yapısı ve içerik türü gösteriliyor. Ölçüt satırlarındaki ifadeler NASA kaynaklarındaki niteliksel bilgilere dayanıyor, sayısal skor değildir.

**Aday:** Haughton Krateri, Devon Adası, Nunavut, Kanada
**Yaklaşık konum:** 75° K, 90° B
**Profil:** Ay üssü
**Görev türü:** Üs operasyonları (görev analoğu)
**Durum:** Bilinen NASA analoğu (doğrulama setinde pozitif örnek)

**Ölçüt dökümü:**

| Ölçüt | Beklenen durum | Dayandığı NASA verisi | NASA kaynağındaki niteliksel bilgi |
|---|---|---|---|
| K1 Kutup aydınlanması | Yüksek | Enlemden hesap | Yüksek Arktik; NASA raporu yaz koşullarını Shackleton kenarının sürekli gün ışığına benzetiyor |
| K2 Kalıcı soğuk | Yüksek | MODIS LST, MERRA-2 | NASA'ya göre dondurucu sıcaklıklar |
| K3 Buz varlığı | Orta–yüksek | MODIS kar/buz | Kutup çölü; Devon Adası'nda buzul kökenli vadi ağları |
| K4 Sırt–krater topografyası | Yüksek | ASTER GDEM | Yaklaşık 20 km çaplı çarpma krateri; istasyon krater kenarında |
| K5 Engebeli ama inilebilir arazi | Orta–yüksek | ASTER GDEM | Kayalık çöl arazisi; gezgin rota planlama deneyleri yapılmış |
| K6 Bitkisizlik | Yüksek | Landsat NDVI | NASA'ya göre çorak arazi |
| K7 Yalıtılmışlık | Çok yüksek | Black Marble | Dünyanın en büyük ıssız adası; yalnızca uçakla erişim |

**Hedefe benzediği yönler:**
- Krater kenarında, birkaç bin kilometrekarelik alanda tek altyapı olan bir üs konumu. NASA bunu Shackleton'da kurulacak bir karakolun konumuna benzetiyor.
- Soğuk, kuru, kayalık ve bitkisiz kutup çölü.
- Shackleton–Malapert gezgin konvoyu simülasyonu yapılmış bir arazi.

**Hedeften farklı olduğu yönler:**
- Atmosfer, yer çekimi ve radyasyon koşulları Ay'dan tamamen farklı.
- Kayalar Ay malzemelerinden çok farklı (NASA raporu bunu kabul ediyor).
- Sıcaklık Ay'ın kalıcı gölgeli bölgelerindeki değerlere hiç yaklaşmıyor.
- Ay'daki gibi "aynı anda bir yanda sürekli aydınlık, diğer yanda sürekli karanlık" ortamı yok. Dünya'da aydınlanma mevsime göre değişiyor.

**Uygun olduğu testler:**
- Basınçlı gezgin ve konvoy operasyonları
- Uzaktan gözlem verisiyle rota planlama ve sahada doğrulama
- Yalıtılmış üs lojistiği
- Uzay giysisiyle saha çalışması provaları

**En yakın bilinen NASA analoğu:** Kendisi (bilinen analog).

### Ek B: Örnek proje özeti (Türkçe taslak)

Aşağıdaki metin, proje sayfası veya sunumun ilk slaytı için bir taslak. Gönderim dili İngilizce olacaksa çevrilmesi gerekecek.

> **Başlık:** Ay Üssü ve Mars İçin Dünya Analogları: NASA Verileriyle Açıklanabilir Bir Benzerlik Haritası
>
> **Özet:** NASA, 2026'da kalıcı Ay üssü için Ay'ın Güney Kutbu'ndaki Shackleton Connecting Ridge'i hedef olarak belirledi. Astronotların ve robotların bu ortama hazırlanması için Dünya'da benzer yerler gerekiyor. Ancak bugün kullanılan analogların çoğu genel olarak "Ay'a benzeyen" yerler. Kutup aydınlanması, buz ve krater kenarı topografyası gibi "Ay üssüne özgü" özellikleri taşıyan analoglar ise çok az.
>
> Projemiz, Ay üssü ve Mars için iki hedef profil tanımlıyor. Ay üssü profilini NASA'nın Lunar Reconnaissance Orbiter verilerinden, Mars profilini NASA'nın Mars Reconnaissance Orbiter, Mars Global Surveyor ve gezgin verilerinden çıkarıyoruz. Ardından Dünya'nın karalarını yalnızca NASA'nın Dünya gözlem verileriyle puanlıyoruz: yükseklik (SRTM, NASADEM, ASTER GDEM, ICESat-2), yüzey görüntüsü (Landsat), mineraller (EMIT), sıcaklık (MODIS), iklim (MERRA-2), yağış (GPM) ve yalıtılmışlık (Black Marble).
>
> Her skor bileşenlerine ayrılabiliyor ve her bileşen hangi NASA verisinden geldiğiyle birlikte gösteriliyor. Model, NASA'nın zaten kullandığı analogları (Haughton Krateri, Atacama Çölü, Salda Gölü ve diğerleri) üst sıralara koyup koymadığına bakılarak doğrulanıyor. Kullanıcı görev türünü (üs operasyonları, kaynak arama, gezgin testi, yaşam algılama, jeoloji eğitimi) seçtiğinde ağırlıklar değişiyor. Böylece aynı yer farklı görevler için farklı skorlar alabiliyor.
>
> Sonuç olarak proje, bilinen analoglardan uzakta yeni aday yerler öneriyor. Her aday için hedefe hangi bakımdan benzediğini ve hangi bakımdan farklı olduğunu açıkça gösteriyor.

### Ek C: Veri indirme kontrol listesi

Hackathon'un ilk saatlerinde aşağıdaki adımlar tamamlanmalı:

**Hesaplar ve erişim:**
- [ ] Her ekip üyesi için NASA Earthdata Login hesabı açıldı.
- [ ] NASA Moon Trek ve Mars Trek erişimi test edildi.
- [ ] NASA PDS'teki LRO ve Artemis II sayfalarına erişim test edildi.

**Ay hedef verileri:**
- [ ] Shackleton Connecting Ridge çevresi için LOLA kutup yükseklik modeli
- [ ] Aynı bölge için Diviner sıcaklık ürünü
- [ ] Aynı bölge için LROC WAC mozaiği
- [ ] LEND hidrojen haritası (kutup bölgesi)
- [ ] Artemis II kullanıcı kılavuzu (kapsanan bölgelerin kontrolü için)

**Mars hedef verileri:**
- [ ] Jezero çevresi için MOLA ve CTX (Mars Trek)
- [ ] Jezero için CRISM mineral ürünü
- [ ] (İsteğe bağlı) Arcadia Planitia için SWIM buz haritası

**Dünya verileri:**
- [ ] Küresel kaba çözünürlüklü yükseklik (SRTM/NASADEM, 60° K – 56° G)
- [ ] Yüksek enlemler için ASTER GDEM
- [ ] Kutup bölgeleri için ICESat-2 ATL14
- [ ] MODIS yüzey sıcaklığı (yıllık ortalamalar için)
- [ ] MODIS kar ve buz örtüsü
- [ ] MERRA-2 iklim değişkenleri
- [ ] GPM IMERG yıllık yağış
- [ ] Landsat veya HLSL30'dan NDVI (bulutsuz bileşik)
- [ ] EMIT mineral ürünü (aday bölgeler için)
- [ ] Black Marble gece ışıkları

**Doğrulama seti:**
- [ ] Bilinen pozitiflerin koordinatları (Haughton, McMurdo, Askja, Mauna Kea, Atacama, Salda, Death Valley, Pilot Valley)
- [ ] Negatif kontrol bölgelerinin seçimi
- [ ] Test vakalarının koordinatları (Wadi Rum, Kapadokya, Bardenas Reales)

### Ek D: Ekip içi iş bölümü önerisi

| Rol | Sorumluluk | Bağlı olduğu bölümler |
|---|---|---|
| Veri sorumlusu | Earthdata, PDS ve Trek'ten veri indirme, kırpma, ortak ızgaraya aktarma | 12, 15.2, Ek C |
| Model sorumlusu | Hedef profiller, ölçüt hesapları, puanlama, ağırlıklar | 13 |
| Doğrulama sorumlusu | Pozitif ve negatif setler, AUC, duyarlılık analizi | 14 |
| Arayüz sorumlusu | Harita, aday listesi, aday kartları, karşılaştırma görselleri | 15.5, Ek A |
| Anlatı sorumlusu | Sunum, proje özeti, kaynak listesi, sınırlılıkların anlatımı | 17, 18, Ek B |

Ekip küçükse veri ve model sorumlulukları birleştirilebilir. Anlatı sorumlusu ise sürecin başından itibaren çalışmalı. Çünkü güçlü bir hikâye, ancak modelin her adımının nedenini bilen biri tarafından yazılabilir.

### Ek E: Jürinin sorabileceği sorular ve hazırlanmış cevaplar

Bu ek, sunum sırasında veya proje değerlendirmesinde gelebilecek soruları ve bu rapora dayanan cevapları içeriyor. Cevaplar kısa tutuldu, böylece sunum sırasında doğrudan kullanılabilir.

**Soru 1: Neden Artemis III iniş bölgeleri yerine Shackleton Connecting Ridge'i hedef aldınız?**
Cevap: Görevin başlığı "kalıcı Ay üssü konumları"ndan söz ediyor. NASA, Moon Base programında ilk robotik görev olan Moon Base I için Shackleton Connecting Ridge'i hedef olarak belirledi. NASA'nın aşamalar sayfası da bu bölgeyi adıyla anıyor. Artemis III bölgeleri birer iniş hedefi, Shackleton Connecting Ridge ise bir üs hedefi. Bu yüzden birincil hedefimiz bu bölge. Artemis III bölgelerini ikincil karşılaştırma için kullanabiliriz.

**Soru 2: Dünya'da Ay'daki kalıcı gölgeli bölgeler gibi 33 Kelvin'lik bir yer yok. O hâlde sıcaklık ölçütünüz ne anlama geliyor?**
Cevap: Haklısınız. Dünya'da bu sıcaklığa yaklaşan doğal bir ortam yok. Bu yüzden sıcaklık ölçütümüz mutlak bir benzerlik değil, göreli bir soğukluk ölçüsü. Yıllık ortalama sıcaklığı düşük, donma günü sayısı yüksek ve kalıcı buz veya kar barındıran yerler daha yüksek puan alıyor. Bu ölçüt "Ay'ın aynısı" değil, "Ay üssünün buz ve soğuk ihtiyaçlarını prova etmeye en uygun" yerleri öne çıkarıyor.

**Soru 3: Neden yalnızca NASA verisi kullandınız?**
Cevap: Bu ekibin bilinçli bir tercihi. Böylece her verinin kaynağı tek bir kurumun açık arşivine dayanıyor ve tekrarlanabilirlik kolaylaşıyor. Ayrıca projenin hem Ay ve Mars tarafındaki hem de Dünya tarafındaki verileri aynı kurumun gözlem ve işleme standartlarına bağlı kalıyor. Bunun bir bedeli var: bazı bölgelerde (örneğin 60° kuzeyin üstünde) SRTM'nin kapsamadığı alanlar için ASTER GDEM ve ICESat-2 gibi alternatif NASA ürünlerine başvurmak zorunda kaldık.

**Soru 4: Modelinizin doğru çalıştığını nasıl biliyorsunuz?**
Cevap: Modeli, NASA'nın zaten analog olarak kullandığı yerlerle sınıyoruz. Ay üssü profili için Haughton Krateri ve McMurdo Kuru Vadileri, Mars profili için Atacama, Salda Gölü, Death Valley ve Pilot Valley gibi yerler bilinen pozitif örnekler. Model bu yerleri rastgele kara hücrelerinden daha yüksek puanlıyorsa ve yoğun orman, tarım alanı veya kent gibi negatif kontrolleri düşük puanlıyorsa doğru çalışıyor demektir. Bunu ROC eğrisi altındaki alan (AUC) ve üst dilim testleriyle ölçüyoruz.

**Soru 5: Ekibinizin başlangıç listesindeki Kapadokya, Wadi Rum ve Bardenas Reales'e ne oldu?**
Cevap: Bu üç yer görsel olarak Ay'a veya Mars'a benziyor ve NASA kaynaklarında da bu yönde tanımlanıyor. Ancak NASA'nın bu yerleri analog olarak kullandığına dair bir kayıt bulamadık. Bu yüzden onları doğrulama setinin pozitif örnekleri arasına almadık. Bunun yerine "test vakası" olarak kullanıyoruz. Modelimizin bunlara verdiği skorlar, görsel benzerlik ile verilerle ölçülmüş benzerlik arasındaki farkı göstermek için iyi bir örnek oluşturuyor.

**Soru 6: Türkiye'den bir analog öneriyor musunuz?**
Cevap: Evet. NASA, Burdur'daki Salda Gölü'nü Perseverance gezgininin incelediği Jezero Krateri'nin analoğu olarak kullanıyor. NASA'ya göre Salda, Jezero'dakilere benzeyen karbonat mineralleri ve delta yapıları barındıran, dünyada bilinen tek göl. Salda, Mars profilimiz için doğrulama setinde bilinen pozitif bir örnek. Modelin Türkiye'deki başka yerler için ne önerdiği ise analiz sonuçlarında görülecek.

**Soru 7: Bir yer neden farklı görev türlerinde farklı puan alıyor?**
Cevap: NASA, analogları jeolojik, astrobiyoloji ve görev analogları olarak üç türe ayırıyor. Bir yer bir tür için çok uygun, başka bir tür için zayıf olabilir. Örneğin Mauna Kea, NASA'nın yerinde kaynak kullanımı testleri için kullandığı bir yer. Kaynak arama görev türünde yüksek puan alabilir. Ama kutup ortamı olmadığı için üs operasyonları görev türünde daha düşük puan alır. Görev türüne göre ağırlıklandırma bu farkı görünür kılıyor.

**Soru 8: "Yeni aday" ne demek? Bu yerleri sahada doğruladınız mı?**
Cevap: "Yeni aday", modelimizin yüksek puan verdiği ve NASA'nın bilinen analoglarından belirli bir uzaklıktan daha uzakta olan yer demek. Bu adayları sahada doğrulamadık. Bu bir hackathon projesi ve sahada doğrulama projenin bir sonraki adımı. Ancak her aday için hangi NASA verisine dayanarak yüksek puan aldığını ve hedeften hangi bakımdan farklı olduğunu açıkça gösteriyoruz. Bu, sahada doğrulama için önceliklendirme yapmayı kolaylaştırıyor.

**Soru 9: Ay ve Dünya verileri arasındaki çözünürlük farkını nasıl ele aldınız?**
Cevap: Küresel taramayı, iklim verileriyle uyumlu kaba bir ızgarada yapıyoruz. Üst sıralara çıkan adayları ise ince çözünürlüklü verilerle (SRTM 30 m, Landsat 30 m, EMIT 60 m) ayrıca inceliyoruz. Topografya karşılaştırmasında hedefi ve adayı aynı ölçekte ölçüyoruz. Örneğin eğim dağılımlarını her iki tarafta da aynı çözünürlüğe indirgeyerek karşılaştırıyoruz.

**Soru 10: Artemis II verilerini nasıl kullandınız?**
Cevap: NASA, Ekim 2026'da Artemis II'nin 800 GB'tan büyük Ay bilimi verisini Planetary Data System'a yükledi. Bu veriler arasında mürettebatın çektiği 11.000'den fazla görüntü var. Bu görüntüleri, önerdiğimiz Dünya analoglarının görsel karşılaştırması için kullanıyoruz. Yörüngeden değil, insan gözünden çekilmiş oldukları için astronotların sahada göreceği manzarayla daha doğrudan bir karşılaştırma sağlıyorlar. Hangi bölgelerin kapsandığını PDS'teki kullanıcı kılavuzundan kontrol ediyoruz.

**Soru 11: Projenizin en büyük sınırlılığı nedir?**
Cevap: Ay üssü profili için NASA'nın kullandığı kutup analoglarının sayısı az. Bu yüzden Ay üssü doğrulamamız, Mars doğrulamamıza göre istatistiksel olarak daha zayıf. İkinci sınırlılık, Dünya'nın Ay'daki vakumu, düşük yer çekimini, uzay radyasyonunu ve aşırı soğuğu taklit edememesi. Modelimiz yalnızca Dünya'da uydudan ölçülebilen özellikleri karşılaştırıyor. Bu sınırlılıkları sunumda ve arayüzde açıkça gösteriyoruz.

**Soru 12: Bu proje NASA'nın Moon Base programına nasıl katkı sağlayabilir?**
Cevap: Moon Base programı, astronotlar gelmeden önce iniş, hareketlilik, iletişim ve kaynak teknolojilerinin test edilmesini öngörüyor. VIPER, PROMISE ve MoonFall gibi görevler buz ve kaynak arayacak. Arazi araçları ve basınçlı gezginler kutup arazisinde hareket edecek. Bu teknolojilerin ve operasyonların Dünya'da prova edilmesi için, Shackleton Connecting Ridge'in özelliklerine benzeyen yerlerin sistematik olarak bulunması gerekiyor. Projemiz, bu arayışı NASA'nın kendi açık verileriyle tekrarlanabilir ve açıklanabilir bir şekilde yapmanın bir yolunu gösteriyor.

---

*Bu rapor, NASA Space Apps Challenge 2026 kapsamında hazırlanmıştır. Bütün bilgiler NASA kaynaklarına dayanmaktadır. Uygunluk notları ekibin niteliksel değerlendirmesidir ve modelin hesaplayacağı skorların yerini tutmaz.*
