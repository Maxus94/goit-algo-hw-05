# goit-algo-hw-05

## Отримані такі результати роботи для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа:

### first file

#### long existing patern: використовувати

1.0302608562633395 - knut_morris_pratt_search  
0.267990211956203 - boyer_moore_search  
2.2907838127575815 - rabin_karp_search

#### short existing patern: або

0.3408358981832862 - knut_morris_pratt_search  
0.21231972379609942 - boyer_moore_search  
0.49172451440244913 - rabin_karp_search

#### middle existing patern: метод

0.5720590809360147 - knut_morris_pratt_search  
0.401095163077116 - boyer_moore_search  
1.3416129741817713 - rabin_karp_search

#### not existing long patern: dffssgdfgtroiogu

2.9106282657012343 - knut_morris_pratt_search  
0.7159925037994981 - boyer_moore_search  
8.767522500827909 - rabin_karp_search

#### not existing short patern: ggf

2.9109658538363874 - knut_morris_pratt_search  
3.504872481804341 - boyer_moore_search  
8.974629587959498 - rabin_karp_search

### second file

#### existing long patern: використовувати

1.18669896107167 - knut_morris_pratt_search  
0.34402960492298007 - boyer_moore_search  
2.9074382237158716 - rabin_karp_search

#### existing short patern: або

1.0974463536404073 - knut_morris_pratt_search  
1.091520054731518 - boyer_moore_search  
2.43682780303061 - rabin_karp_search

#### middle existing patern: метод

0.003622564021497965 - knut_morris_pratt_search  
0.005921901203691959 - boyer_moore_search  
0.014923880342394114 - rabin_karp_search

#### not existing long patern: dffssgdfgtroiogu

4.142800800036639 - knut_morris_pratt_search  
0.9983765720389783 - boyer_moore_search  
12.682195589877665 - rabin_karp_search

#### not existing short patern: ggf

4.099929695948958 - knut_morris_pratt_search  
5.146795773878694 - boyer_moore_search  
12.713293267879635 - rabin_karp_search

Проведено дослідженні поведінки методів Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа при пошуку різних підрядків в двох різних текстах. Проведено пошук в двох файлах довгого, середньої довжини та короткого зразку, що зустрічається в цих файлах та довгого й короткого зразків, що в файлах не зустрічаються. В переважній більшості випадків найшвидшим виявився метод Боєра-Мура. Найповільнішим виявився метод Рабіна-Карпа. У випадку пошуку короткого неіснуючого підрядка з трьох літер в тексті, найшвидшим виявився метод Кнута-Морріса-Пратта для обох файлів, швидкість пошуку цього методу не залежить від довжини зразка.
