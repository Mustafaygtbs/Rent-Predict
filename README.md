# Ankara Emlak Fiyat Tahmini Projesi

## Proje Özeti

Bu proje, Ankara'daki kiralık konut fiyatlarını tahmin eden bir makine öğrenimi modeli geliştirme ve web uygulaması olarak sunma sürecini kapsamaktadır. Hepsiemlak ve Sahibinden.com platformlarından veri çekilerek oluşturulan veri seti, kapsamlı ön işleme adımlarından geçirilmiş ve Gradient Boosting Regressor algoritması ile eğitilmiştir. Flask web çerçevesi kullanılarak, kullanıcı dostu bir arayüz ile model tahminleri herkesin erişimine sunulmuştur.

**Not:** Bu projede web scraping ile toplanan veriler yalnızca eğitim amaçlı kullanılmıştır. Ticari amaçla kullanılmamıştır.

## Proje Aşamaları

### 1. Veri Toplama (Web Scraping)

Projenin ilk adımında Selenium ve BeautifulSoup kütüphaneleri kullanılarak web scraping işlemi gerçekleştirilmiştir:

- **Veri Kaynakları:** Hepsiemlak ve Sahibinden.com
- **Çekilen Veriler:** Ankara'daki kiralık konut ilanları (fiyat, oda sayısı, metrekare, bina yaşı, konum bilgileri)
- **Dinamik Sayfa Yükleme:** Selenium ile sayfa etkileşimleri otomatize edilmiştir
- **Anti-Bot Önlemleri:** Rasgele bekleme süreleri ve gerçek kullanıcı ajanı tanımlamaları eklenmiştir

### 2. Veri Ön İşleme

Toplanan ham veriler kapsamlı bir ön işleme sürecinden geçirilmiştir:

- **Veri Temizleme:** Gereksiz sütunlar çıkarılmış, eksik değerler analiz edilmiştir
- **Veri Dönüşümü:** Fiyat gibi metin formatındaki sayısal veriler uygun tiplere dönüştürülmüştür
- **Konum Verisi İşleme:** İlçe ve mahalle bilgileri ayrıştırılmıştır
- **Veri Birleştirme:** Farklı kaynaklardan gelen veriler tek bir tutarlı veri setinde bir araya getirilmiştir

### 3. Aykırı Değer Tespiti ve Temizleme

Veri setindeki aykırı değerler DBSCAN algoritması kullanılarak tespit edilmiştir:

- **Kümeleme Tabanlı Yaklaşım:** Standartlaştırılmış veriler üzerinde DBSCAN uygulanmıştır
- **Analiz Edilen Özellikler:** Fiyat, metrekare ve bina yaşı özellikleri kullanılmıştır
- **Temizleme:** 3,406 kayıttan 13 aykırı değer çıkarılarak 3,393 kayıtlık temiz bir veri seti elde edilmiştir

### 4. Eksik Değer Doldurma

Veri setindeki eksik değerler, özellikle bina yaşı için, akıllı bir strateji ile doldurulmuştur:

- **Hiyerarşik Doldurma Stratejisi:** 
  1. Aynı ilçe ve mahallede bulunan konutların ortalama değerleri 
  2. Aynı ilçedeki konutların ortalama değerleri
  3. Genel veri seti ortalaması

- **Oda Sayısı İşleme:** "3+1" gibi formatlar toplamları alınarak sayısal değerlere dönüştürülmüştür

### 5. Model Eğitimi

Temizlenen ve hazırlanan veri seti üzerinde Gradient Boosting Regressor modeli eğitilmiştir:

- **Özellik Mühendisliği:** Sayısal ve kategorik özellikler için uygun dönüşümler uygulanmıştır
- **Pipeline Yaklaşımı:** Veri ön işleme ve model eğitimi tek bir pipeline'da birleştirilmiştir
- **Hiperparametre Optimizasyonu:** GridSearchCV ile en iyi model parametreleri belirlenmiştir
- **Çapraz Doğrulama:** 5-katlı çapraz doğrulama ile model değerlendirilmiştir
- **Model Performansı:** 
  - RMSE: 6,814.53 (eğitim), 7,044.29 (test)
  - MAE: 4,796.70
  - R² Skoru: 0.6276

### 6. Web Uygulaması Geliştirme

Eğitilen model, Flask web çerçevesi kullanılarak kullanıcı dostu bir web uygulaması haline getirilmiştir:

- **Kullanıcı Arayüzü:** Bootstrap ile modern, duyarlı bir tasarım oluşturulmuştur
- **Dinamik Form:** İlçe seçimine göre dinamik olarak güncellenen mahalle listesi
- **AJAX İstekleri:** Sayfa yenilenmesi olmadan gerçek zamanlı tahminler
- **Görselleştirme:** Kullanıcı dostu sonuç ekranı

### 7. Uygulama Optimizasyonu ve Hata Ayıklama

Uygulama ayağa kaldırıldıktan sonra performans ve kullanıcı deneyimini iyileştirmek için çeşitli adımlar atılmıştır:

- **Scikit-learn Sürüm Uyumluluğu:** Model ve uygulama arasındaki sürüm farklılıkları giderilmiştir
- **JavaScript Hata Ayıklama:** AJAX isteklerindeki JSON yanıt sorunları düzeltilmiştir
- **Dosya Erişim Sorunları:** Statik dosya erişimi optimize edilmiştir

## Teknik Detaylar

### Kullanılan Teknolojiler

- **Veri Toplama:** Selenium, BeautifulSoup, Python requests
- **Veri İşleme:** Pandas, NumPy
- **Makine Öğrenimi:** Scikit-learn, XGBoost
- **Web Geliştirme:** Flask, jQuery, Bootstrap
- **Görselleştirme:** Matplotlib, Seaborn

### Model Performansı

Gradient Boosting Regressor modeli, emlak fiyatlarındaki varyasyonun %62.76'sını açıklayabilen güçlü bir tahmin performansı göstermiştir. Metrekare, ilçe, mahalle ve oda sayısı tahminlerde en etkili özellikler olarak belirlenmiştir.


## Sonuç

Bu proje, veri bilimi ve makine öğrenimi becerilerini gerçek dünya problemi üzerinde uygulama fırsatı sunmuştur. Web scraping'den model eğitimine ve web uygulaması geliştirmeye kadar tüm aşamaları kapsayan bu çalışma, sınırlı veri kaynağına rağmen %62.76 R² skoru elde ederek Ankara'daki kiralık konut fiyatlarının tahmininde kayda değer bir başarı göstermiştir.

---

*Bu projede web scraping ile toplanan veriler yalnızca eğitim amaçlı kullanılmıştır ve ticari amaçla kullanılmamıştır. Proje kapsamında toplanan verilerin telif hakları ilgili platformlara aittir.*
