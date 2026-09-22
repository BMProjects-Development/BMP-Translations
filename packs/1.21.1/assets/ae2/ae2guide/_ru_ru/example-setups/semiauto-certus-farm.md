---
navigation:
  parent: example-setups/example-setups-index.md
  title: Полуавтоматическая ферма кварца
  icon: certus_quartz_crystal
  position: 115
---

# Полуавтоматическая ферма кварца

К сожалению, для полноценной автоматической работы [простой фермы кварца](simple-certus-farm.md) требуется <ItemLink id="flawless_budding_quartz" />. Для этого требуется либо [Пространственное ИО](../ae2-mechanics/spatial-io.md), либо построить ферму на [метеорите](../ae2-mechanics/meteorites.md).

Однако AE2 может размещать и ломать блоки, поэтому,
можно сделать так, чтобы ваша ферма *заменяла цветущий истинный кварц*. (Для этого придется периодически вставлять некоторые
<ItemLink id="flawed_budding_quartz" /> во входную бочку и извлекать <ItemLink id="quartz_block" /> из обработаной бочки).

Чтобы сделать это полностью автоматически, смотрите [Улучшенная ферма кварца](advanced-certus-farm.md).

Эта ферма немного сложнее, чем [простая ферма кварца](simple-certus-farm.md), поскольку фактически представляет собой
3 отдельные установки, объединенные вместе.

**ЭТО СЛОЖНАЯ КОНСТРУКЦИЯ, В КОТОРОЙ ВЕЩИ СПРЯТАНЫ ЗА ДРУГИМИ ВЕЩАМИ, ПОКРУТИТЕСЬ ВОКРУГ, ЧТОБЫ РАССМОТРЕТЬ ЕЕ СО ВСЕХ СТОРОН**.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/semiauto_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) Плоскость уничтожения # 1: Не имеет графического интерфейса для настройки, но может быть зачарована на удачу.
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1" max="2.3 3 2">
        (2) Шина хранения #1: Фильтруется на кристалл истинного кварца.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    Подсеть кластера-разрушителя
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) Плоскость уничтожения #2: Нет графического интерфейса для настройки, но может быть зачарована на шелковое касание.
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1" max="2.3 2 2">
        (4) Шина хранения #2: Отфильтрована до блока истинного кварца.
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    Подсеть для разрушения блоков истинного кварца
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) Плоскость формирования: В конфигурации по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0 1" max="2.3 1 2">
        (6) Шина импорта: В конфигурации по умолчанию.
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    Подсеть для установки зарождающихся блоков
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="0.7 2 1" max="1 3 2">
        (7) Шина хранения #3: Отфильтрована до кристалла истинного кварца. Приоритет выше, чем у основного хранилища.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

    <DiamondAnnotation pos="1.5 0.5 1.5" color="#00ff00">
        Ручная установка несовершенного зарождающегося истинного кварца.
        <BlockImage id="flawed_budding_quartz" scale="2" />
    </DiamondAnnotation>

    <DiamondAnnotation pos="1.5 1.5 1.5" color="#00ff00">
        Ручное извлечение блока истинного кварца
        <BlockImage id="quartz_block" scale="2" />
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="165" pitch="5" />
</GameScene>

## Конфигурации

### Кластерный разрушитель:

* Первая <ItemLink id="annihilation_plane" /> (1) не имеет графического интерфейса и не может быть настроена, но может быть зачарована на Удачу.
* Первая <ItemLink id="storage_bus" /> (2) фильтруется на <ItemLink id="certus_quartz_crystal" />.

### Разрушитель блоков истинного кварца:

* Вторая <ItemLink id="annihilation_plane" /> (3) не имеет графического интерфейса и не может быть настроена, но должен быть зачарована на шелковое касание.
* Вторая <ItemLink id="storage_bus" /> (4) фильтруется на <ItemLink id="quartz_block" />.

### Установщик зарождающихся блоков:

* <ItemLink id="formation_plane" /> (5) находится в конфигурации по умолчанию.
* <ItemLink id="import_bus" /> (6) имеет конфигурацию по умолчанию.

### В основной сети:

* Третяя <ItemLink id="storage_bus" /> (7) фильтруется на <ItemLink id="certus_quartz_crystal" />, и имеет свой
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) установлен выше, чем у основного хранилища.

## Как это работает

### Кластерный разрушитель:

Подсеть разрушителя кластера работает аналогично подсети в [простой ферме кварца](simple-certus-farm.md).

1. Подсеть <ItemLink id="annihilation_plane" /> пытается разрушить то, что находится перед ней, но может разрушить только <ItemLink id="quartz_cluster" />.
   поскольку единственным хранилищем в подсети является <ItemLink id="formation_plane" />, отфильтрованная до <ItemLink id="certus_quartz_crystal" />.
2. В <ItemLink id="storage_bus" /> хранятся кристаллы истинного кварца в бочке.

### Разрушитель блоков истинного кварца/

Подсеть разрушителя блоков истинного кварца служит для разрушения поврежденного цветущего блока, когда он превращается в обычный <ItemLink id="quartz_block" />.
Она работает аналогично разрушителю кластеров.

1. Подсеть <ItemLink id="annihilation_plane" /> пытается разрушить то, что находится перед ней, но может разрушить только <ItemLink id="quartz_block" />.
   поскольку единственным хранилищем в подсети является <ItemLink id="formation_plane" />, отфильтрованная до <ItemLink id="quartz_block" />.
   Плоскость должна иметь шелковое касание, чтобы при разрушении блок не разрушился, и, соответственно, плоскость не разрушила его преждевременно.
2. В <ItemLink id="storage_bus" /> хранится блок истинного кварца
   Для того чтобы обновить его, необходимо вручную бросить его в воду с помощью <ItemLink id="charged_certus_quartz_crystal" />.

### Установщик зарождающихся блоков

Подсеть служит для размещения нового <ItemLink id="flawed_budding_quartz" />, когда разрушающая подсеть разбивает старый, поврежденный.

1. Подсеть <ItemLink id="import_bus" /> импортирует цветущий блок из входного ствола.
2. Единственным хранилищем в подсети является <ItemLink id="formation_plane" />, в котором размещается цветущий блок.

### В основной сети

* <ItemLink id="storage_bus" /> предоставляет основной сети (а также [автоматизации зарядника](charger-automation.md)) доступ ко всем кристаллам истинного кварца, находящимся в бочке. Для него установлен
высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority), чтобы кристаллы истинного кварца приоритетно
помещались обратно в бочку, а не в основное хранилище.