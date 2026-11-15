/* Atlas saha fotoğrafları. Her görsel, sahanın kartta anlatılan özelliğini gösterecek biçimde seçildi;
   konum, açıklama ve lisans Wikimedia Commons kaydından kontrol edildi. Görseller Commons'tan yüklenir
   ve kartta sahibi, lisansı ve kaynak sayfasıyla gösterilir. Bu dosya bilimsel veri değildir.
   Alanlar: src, page, w, h, artist, license, cap {tr, en}, pos (isteğe bağlı kırpma odağı). */
(function () {
  const C = 'https://thumb.wikimedia.org/wikipedia/commons/thumb/';
  const F = 'https://commons.wikimedia.org/wiki/File:';
  const U = 'https://upload.wikimedia.org/wikipedia/commons/';
  const p = (src, file, w, h, artist, license, tr, en, pos) => ({ src, page: F + file, w, h, artist, license, cap: { tr, en }, pos: pos || '' });
  window.TT_PHOTOS = {
    haughton: p(C + '0/05/Rovers_Red_and_Black_at_Houghton_Crater_Devon_Island_Canada.jpg/960px-Rovers_Red_and_Black_at_Houghton_Crater_Devon_Island_Canada.jpg', 'Rovers_Red_and_Black_at_Houghton_Crater_Devon_Island_Canada.jpg', 960, 720, 'NASA', 'Kamu malı',
      'NASA gezginleri Haughton Krateri’nde saha testinde', 'NASA rovers during a field test at Haughton Crater'),
    salda: p(C + '3/3b/SaldaLake8.jpg/960px-SaldaLake8.jpg', 'SaldaLake8.jpg', 960, 700, 'Ahmet Emre Öz', 'CC BY-SA 4.0',
      'Salda Gölü kıyısında beyaz hidromagnezit tortulları', 'White hydromagnesite deposits on the shore of Lake Salda'),
    mcmurdo: p(C + '3/35/Wright_Valley_From_Bull_Pass.jpg/960px-Wright_Valley_From_Bull_Pass.jpg', 'Wright_Valley_From_Bull_Pass.jpg', 960, 640, 'David Saul', 'Kamu malı',
      'Kuru Vadiler’den Wright Vadisi, Bull Geçidi’nden batıya bakış', 'Wright Valley in the Dry Valleys, looking west from Bull Pass'),
    atacama: p(C + 'd/d5/Patterned_ground_located_in_the_Atacama_Desert_%28Chile%29.jpg/960px-Patterned_ground_located_in_the_Atacama_Desert_%28Chile%29.jpg', 'Patterned_ground_located_in_the_Atacama_Desert_(Chile).jpg', 960, 720, 'Christof 123456', 'CC BY-SA 4.0',
      'Atacama’nın hiper-kurak çekirdeğinde (Yungay yakını) poligonal toprak deseni', 'Polygonal patterned ground in the Atacama’s hyper-arid core near Yungay'),
    askja: p(U + 'e/e6/Askja.jpg', 'Askja.jpg', 640, 428, 'Michael Ryan', 'Kamu malı',
      'Askja kalderası ve Öskjuvatn gölü', 'Askja caldera and lake Öskjuvatn'),
    maunakea: p(C + '8/8c/Pu%27u_on_Mauna_Kea.jpg/960px-Pu%27u_on_Mauna_Kea.jpg', "Pu'u_on_Mauna_Kea.jpg", 960, 640, 'S P Schmidt', 'CC BY 4.0',
      'Mauna Kea zirvesinde cüruf konileri ve ince volkanik malzeme', 'Cinder cones and fine volcanic material on the summit of Mauna Kea'),
    deathvalley: p(C + '2/2b/Research_Drone_Flies_Over_Mars_Hill_%28PIA26676%29.jpg/960px-Research_Drone_Flies_Over_Mars_Hill_%28PIA26676%29.jpg', 'Research_Drone_Flies_Over_Mars_Hill_(PIA26676).jpg', 960, 1440, 'NASA/JPL-Caltech', 'Kamu malı',
      'Ölüm Vadisi’ndeki Mars Hill: NASA JPL test dronu iri bloklu volkanik arazinin üzerinde (2025)', 'Mars Hill in Death Valley: a NASA JPL test drone over blocky volcanic terrain (2025)', 'center 42%'),
    kilauea: p(C + '7/7e/WalkingonIki.jpg/960px-WalkingonIki.jpg', 'WalkingonIki.jpg', 960, 640, 'Relativity', 'CC BY-SA 4.0',
      'Kīlauea Iki krater tabanında bazalt lav yüzeyi', 'Basaltic lava surface on the floor of Kīlauea Iki crater'),
    medicine: p(C + 'f/f2/Valentine_Cave.JPG/960px-Valentine_Cave.JPG', 'Valentine_Cave.JPG', 960, 640, 'Dave Bunnell / Under Earth Images', 'CC BY-SA 2.5',
      'Lava Beds’te Valentine Mağarası lav tüpü', 'Valentine Cave, a lava tube at Lava Beds'),
    pilot: p(C + '1/1b/Pilot_Range_Along_Nevada_and_Utah_%2850419432496%29.jpg/960px-Pilot_Range_Along_Nevada_and_Utah_%2850419432496%29.jpg', 'Pilot_Range_Along_Nevada_and_Utah_(50419432496).jpg', 960, 640, 'formulanone', 'CC BY-SA 2.0',
      'Pilot Dağları, havadan; Pilot Vadisi playası bu dağların doğu eteğindedir', 'The Pilot Range from the air; the Pilot Valley playa lies at its eastern foot'),
    katmai: p(C + '7/7c/Ten_Thousand_Smokes_Valley_-_panoramio_%281%29.jpg/960px-Ten_Thousand_Smokes_Valley_-_panoramio_%281%29.jpg', 'Ten_Thousand_Smokes_Valley_-_panoramio_(1).jpg', 960, 595, 'Eric Spenle', 'CC BY 3.0',
      'On Bin Duman Vadisi’nin 1912 kül dolgusu', 'The 1912 ash fill of the Valley of Ten Thousand Smokes'),
    kapadokya: p(C + '4/42/Fairy_chimneys_in_Cappadocia.JPG/960px-Fairy_chimneys_in_Cappadocia.JPG', 'Fairy_chimneys_in_Cappadocia.JPG', 960, 641, 'Wolfgang Moroder', 'CC BY-SA 3.0',
      'Kapadokya’da aşınmış volkanik tüften peri bacaları', 'Fairy chimneys of eroded volcanic tuff in Cappadocia'),
    wadirum: p(C + '5/56/Mountain_in_Wadi_Rum%2C_Jordan.jpg/960px-Mountain_in_Wadi_Rum%2C_Jordan.jpg', 'Mountain_in_Wadi_Rum,_Jordan.jpg', 960, 638, 'Daniel Case', 'CC BY-SA 3.0',
      'Wadi Rum’da kırmızı kum ve kumtaşı kütle', 'Red sand and a sandstone massif in Wadi Rum'),
    bardenas: p(C + '1/10/Castildetierra_-_Summer_morning.jpg/960px-Castildetierra_-_Summer_morning.jpg', 'Castildetierra_-_Summer_morning.jpg', 960, 641, 'Ant°AM', 'CC BY-SA 4.0',
      'Bardenas Reales’te Castildetierra kil ve kumtaşı oluşumu', 'The Castildetierra clay-and-sandstone formation in Bardenas Reales'),
    nemrut: p(C + '4/41/Nemrut_Da%C4%9F%C4%B1_25_05_2010_Caldera.jpg/960px-Nemrut_Da%C4%9F%C4%B1_25_05_2010_Caldera.jpg', 'Nemrut_Da%C4%9F%C4%B1_25_05_2010_Caldera.jpg', 960, 689, 'Volker Höhfeld', 'CC BY-SA 4.0',
      'Nemrut Kalderası: güney kenardan kaldera tabanına ve Nemrut Gölü’ne bakış', 'Nemrut Caldera: view from the southern rim to the caldera floor and lake'),
    tuz: p(C + 'c/ca/Tuz_G%C3%B6l%C3%BC_2.jpg/960px-Tuz_G%C3%B6l%C3%BC_2.jpg', 'Tuz_G%C3%B6l%C3%BC_2.jpg', 960, 640, 'Wokege', 'CC0',
      'Tuz Gölü’nün kuruyan tuz kabuğu', 'The drying salt crust of Lake Tuz'),
    harrat: p(C + '4/4c/%D8%AD%D8%B1%D8%A9_%D8%AE%D9%8A%D8%A8%D8%B1.jpg/960px-%D8%AD%D8%B1%D8%A9_%D8%AE%D9%8A%D8%A8%D8%B1.jpg', '%D8%AD%D8%B1%D8%A9_%D8%AE%D9%8A%D8%A8%D8%B1.jpg', 960, 1066, 'NASA Earth Observatory (Landsat)', 'Kamu malı',
      'Harrat Khaybar’da açık renkli kül ve koyu lav birimleri, NASA Landsat görüntüsü (2024)', 'Light ash and dark lava units at Harrat Khaybar, NASA Landsat image (2024)'),
    pinacate: p(C + 'e/e9/Reserva_de_la_Biosfera_El_Pinacate%2C_Sonora-Biosphere_Reserve%2C_El_Pinacate%2C_Sonora_%2823107632322%29.jpg/960px-Reserva_de_la_Biosfera_El_Pinacate%2C_Sonora-Biosphere_Reserve%2C_El_Pinacate%2C_Sonora_%2823107632322%29.jpg', 'Reserva_de_la_Biosfera_El_Pinacate,_Sonora-Biosphere_Reserve,_El_Pinacate,_Sonora_(23107632322).jpg', 960, 639, 'Comisión Mexicana de Filmaciones', 'CC BY-SA 2.0',
      'El Pinacate’nin büyük maar kraterlerinden biri', 'One of El Pinacate’s large maar craters'),
    makgadikgadi: p(C + 'c/c6/Salar_del_parque_nacional_Makgadikgadi_Pans%2C_Botsuana%2C_2018-07-30%2C_DD_37.jpg/960px-Salar_del_parque_nacional_Makgadikgadi_Pans%2C_Botsuana%2C_2018-07-30%2C_DD_37.jpg', 'Salar_del_parque_nacional_Makgadikgadi_Pans,_Botsuana,_2018-07-30,_DD_37.jpg', 960, 357, 'Diego Delso', 'CC BY-SA 4.0',
      'Makgadikgadi’de eski göl tabanının tuz kabuğu', 'The salt crust of the ancient lake bed at Makgadikgadi'),
    hanksville: p(C + '4/49/Mars_Desert_Research_Station_2020.jpg/960px-Mars_Desert_Research_Station_2020.jpg', 'Mars_Desert_Research_Station_2020.jpg', 960, 640, 'The Mars Society / MDRS', 'CC BY-SA 4.0',
      'Hanksville yakınındaki Mars Çöl Araştırma İstasyonu ve kızıl kötü topraklar', 'The Mars Desert Research Station and red badlands near Hanksville'),
    pilbara: p(C + '2/2f/Stromatolite_%28Dresser_Formation%2C_Paleoarchean%2C_3.48_Ga%3B_Normay_Mine%2C_North_Pole_Dome%2C_Pilbara_Craton%2C_Western_Australia%29_1_%2832857204117%29.jpg/960px-Stromatolite_%28Dresser_Formation%2C_Paleoarchean%2C_3.48_Ga%3B_Normay_Mine%2C_North_Pole_Dome%2C_Pilbara_Craton%2C_Western_Australia%29_1_%2832857204117%29.jpg', 'Stromatolite_(Dresser_Formation,_Paleoarchean,_3.48_Ga;_Normay_Mine,_North_Pole_Dome,_Pilbara_Craton,_Western_Australia)_1_(32857204117).jpg', 960, 715, 'James St. John', 'CC BY 2.0',
      'Pilbara’dan 3,48 milyar yıllık stromatolit (Dresser Formasyonu, North Pole Dome)', 'A 3.48-billion-year-old stromatolite from the Pilbara (Dresser Formation, North Pole Dome)')
  };
})();
