---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоблокировка интерфейса
  icon: interface
---

# Автоблокировка интерфейса

Возникает вопрос: "Как поддерживать определенное количество различных предметов на складе, создавая новые по мере необходимости?".

Одним из решений является использование <ItemLink id="interface" /> и <ItemLink id="crafting_card" /> для автоматического запроса новых предметов
из сети [автокрафта](../ae2-mechanics/autocrafting.md). Эта настройка больше подходит для поддержания небольшого количества
разнообразных предметов.

Эта демонстрационная установка урезана, чтобы не быть слишком широкой, скорее всего, наиболее оптимально использовать 4 <ItemLink id="interface" /> и 4 <ItemLink id="storage_bus" />,
использовать все 8 [каналов](../ae2-mechanics/channels.md) в обычном [кабеле](../items-blocks-machines/cables.md).

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_autostocking.snbt" />

<BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
        (1) Интерфейсы: Набор для хранения нужных предметов в себе. У них есть карты изготовления.
        <ItemImage id="crafting_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
        (2) Шины хранения: "Режим ввода/вывода" установлен на "Только извлечение".
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации
* Элементы <ItemLink id="interface" /> (1) настраиваются на удержание нужных элементов в себе, для чего необходимо щелкнуть нужный элемент в их верхних слотах
или перетащить в верхние слоты из JEI, а затем щелкнуть на значке гаечного ключа над слотами, чтобы установить количество. Содержат <ItemLink id="crafting_card" />.
* <ItemLink id="storage_bus" /> (2) установлены таким образом, что "Режим ввода/вывода" установлен на "Только извлечение".

## Как это работает

1. Если <ItemLink id="interface" /> не может получить достаточное количество сконфигурированного элемента из [хранилища сети](../ae2-mechanics/import-export-storage.md),
   (и у него есть <ItemLink id="crafting_card" />), он запросит у сетевого [автокрафта](../ae2-mechanics/autocrafting.md) создание большего количества этого предмета.
2. <ItemLink id="storage_bus" /> позволяет сети получить доступ к содержимому интерфейсов.