---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматизация обогащения руд
  icon: minecraft:raw_iron
---

# Автоматизация обогащения руд

На <ItemLink id="annihilation_plane" /> может быть наложено любое зачарование кирки, в том числе удача, поэтому очевидным вариантом использования будет
применить удачу к некоторым из них и заставить <ItemLink id="formation_plane" /> и <ItemLink id="annihilation_plane" /> быстро размещать и
разбивать руды.

Обратите внимание, что поскольку <ItemLink id="import_bus" /> "раскручивается до скорости", установка начнется медленно, а затем достигнет полной скорости за несколько секунд.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/ore_fortuner.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 0 2" max="3 1 3">
        (1) Шина импорта: Имеет несколько карт ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 2" max="2 1 2.3">
        (2) Плоскости формирования: В конфигурации по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 0.7" max="2 1 1">
        (3) Плоскости уничтожения: Отсутствие графического интерфейса для настройки, но зачарование на удачу.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 0 0" max="3 1 1">
        (4) Шина хранения: В конфигурации по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="3.5 0.5 2.5" color="#00ff00">
        Ввод
    </DiamondAnnotation>

<DiamondAnnotation pos="3.5 0.5 0.5" color="#00ff00">
        Вывод
    </DiamondAnnotation>

<DiamondAnnotation pos="4 0.5 1.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации

* В конфигурации <ItemLink id="import_bus" /> (1) имеется несколько <ItemLink id="speed_card" />. Их потребуется столько, сколько плоскостей формирования
в массиве, так как они заставляют шину импорта тянуть больше элементов одновременно.
* <ItemLink id="formation_plane" /> (2) находятся в конфигурации по умолчанию.
* <ItemLink id="annihilation_plane" /> (3) не имеют графического интерфейса и не могут быть настроены, но зачарованы на удачу.
* <ItemLink id="storage_bus" /> (4) имеет конфигурацию по умолчанию.

## Как это работает

1.  Шина <ItemLink id="import_bus" /> в зеленой подсети импортирует блоки из первой бочки в [хранилище сети](../ae2-mechanics/import-export-storage.md).
2.  Единственным хранилищем в зеленой подсети является <ItemLink id="formation_plane" />, в котором размещаются блоки.
3.  Хранилище <ItemLink id="annihilation_plane" /> в оранжевой подсети разбивает блоки, применяя к ним удачу.
4.  Система <ItemLink id="storage_bus" /> в оранжевой подсети сохраняет результаты разбивания во второй бочке.