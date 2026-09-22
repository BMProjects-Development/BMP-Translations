---
navigation:
  parent: example-setups/example-setups-index.md
  title: Продвинутая ферма кварца
  icon: certus_quartz_crystal
  position: 120
---

# Продвинутая ферма кварца

По сути, это просто [полуавтоматическая ферма кварца](semiauto-certus-farm.md), а исключением того, что она полностью интегрирована в вашу
МЭ систему.

Вместо того, чтобы иметь большой запас начинающих блоков и вручную обновлять их время от времени,
эта установка использует [автоматическую зарядку](charger-automation.md) и [автоматицазию изготовления при бросках в воду](throw-in-water-automation.md)
для автоматической работы.

**ЭТО СЛОЖНАЯ СБОРКА, В КОТОРОЙ ВСЕ СПРЯТАНО ЗА ДРУГИМИ ВЕЩАМИ, ПОКРУТИТЕСЬ ВОКРУГ, ЧТОБЫ РАССМОТРЕТЬ ЕЕ СО ВСЕХ СТОРОН**.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/advanced_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) Плоскость уничтожения #1: Не имеет графического интерфейса для настройки, но может быть зачарована на удачу..
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1.7" max="3 3 2">
        (2) Шина хранения #1: Фильтруется до кристалла истинного кварца
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    Подсеть кластера-разрушителя
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) Плоскость уничтожения #2: Отсутствие графического интерфейса для настройки, но зачарованный на шелковое касание.
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1.7" max="3 2 2">
        (4) Шина хранения #2: Фильтруется до блока истинного кварца.
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    Подсеть разрушения блоков истинного кварца
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) Плоскость формирования: В конфигурации по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0.7 2" max="3 1 3">
        (6) Шина импорта: Отфильтрованный до несовершенного ростка истинного кварца
        <BlockImage id="flawed_budding_quartz" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    Подсеть установщика зарождающегося блока
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="1.7 2 2" max="2 3 3">
        (7) Шина хранения #3: Отфильтрован до кристалла истинного кварца. Приоритет выше, чем у основного хранилища.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#aaaadd" min="2 1 2" max="3 2 3">
        (8) Интерфейс: Удерживает в себе 1 несовершенный зарождающийся истинный кварц, имеет карту крафта.
        <Row><BlockImage id="flawed_budding_quartz" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="1.5 0.5 0" color="#00ff00">
        К основной сети, автоматизация зарядника и автоматизация бросков в воду
        <Row>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        </Row>
    </DiamondAnnotation>

  <IsometricCamera yaw="165" pitch="5" />
</GameScene>

## Конфигурации

### Кластерный разрушитель:

* Первая <ItemLink id="annihilation_plane" /> (1) не имеет графического интерфейса и не может быть настроен, но может быть зачарован на удачу.
* Первая <ItemLink id="storage_bus" /> (2) фильтруется на <ItemLink id="certus_quartz_crystal" />.

### Разрушитель блока истинного кварца

* Вторая <ItemLink id="annihilation_plane" /> (3) не имеет графического интерфейса и не может быть настроен, но должен быть зачарован на шёлковое касание.
* Вторая <ItemLink id="storage_bus" /> (4) фильтруется на  <ItemLink id="quartz_block" />.

### Установщик зарождающегося блока:

* <ItemLink id="formation_plane" /> (5) находится в конфигурации по умолчанию.
* <ItemLink id="import_bus" /> (6) фильтруется на  <ItemLink id="flawed_budding_quartz" />.

### В основной сети

* Третья <ItemLink id="storage_bus" /> (7) фильтруется на <ItemLink id="certus_quartz_crystal" />, и имеет свой
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) становлен выше, чем у основного хранилища.	
* <ItemLink id="interface" /> (8) настроен на хранение в себе 1 потресканного цветущего блока истинного кварца и имеет <ItemLink id="crafting_card" />.

## Как это работает.

### Кластерный разрушитель:

Подсеть разрушителя кластеров работает аналогично подсети в [простой ферме кварца](simple-certus-farm.md).

1. Подсеть <ItemLink id="annihilation_plane" /> пытается разрушить то, что находится перед ней, но может разрушить только <ItemLink id="quartz_cluster" />
   Поскольку единственным хранилищем в подсети является <ItemLink id="formation_plane" />, отфильтрованный до <ItemLink id="certus_quartz_crystal" />.
2. В <ItemLink id="storage_bus" /> хранятся кристаллы истинного кварца в бочке.

### Разрушитель блока истинного кварца

Подсеть служит для разрушения цветущего блока, когда он превращается в обычный <ItemLink id="quartz_block" />.
Она работает аналогично разрушителю кластеров.

1. Подсеть <ItemLink id="annihilation_plane" /> пытается разрушить то, что находится перед ней, но может разрушить только <ItemLink id="quartz_block" />
   поскольку единственным хранилищем в подсети является <ItemLink id="formation_plane" />, отфильтрованный до <ItemLink id="quartz_block" />. 
  Плоскость должна иметь шелковое касание, чтобы при разрушении блок не разрушился, и, соответственно, плоскость не разрушила его преждевременно.
2. В <ItemLink id="storage_bus" /> хранится блок истинного кварца в <ItemLink id="interface" />, что позволяет.
   [Автоматизация бросков в воду](throw-in-water-automation.md) использовать его для создания нового <ItemLink id="flawed_budding_quartz" />.

### Установщик зарождающегося блока:

Установщик служит для размещения новой подсети <ItemLink id="flawed_budding_quartz" /> при разрушении старой исчерпавшей себя подсети.

1. Подсеть <ItemLink id="import_bus" /> импортирует зарождающийся блок из <ItemLink id="interface" /> в [хранилище сети](../ae2-mechanics/import-export-storage.md)
2. Единственным хранилищем в подсети является <ItemLink id="formation_plane" />, в которое помещается цветущий блок.

### В основной сети

*<ItemLink id="storage_bus" /> предоставляет основной сети (а также [Автоматический зарядние](charger-automation.md)) доступ ко всем кристаллам истинного кварца в бочке. Для него установлен
  высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) чтобы кристаллы истинного кварца предпочтительно
  помещались обратно в бочку, а не в основное хранилище.
* <ItemLink id="interface" /> предоставляет подсети, занимающейся размещением блоков, доступ к <ItemLink id="flawed_budding_quartz" />, и
    дает подсети разрушителя блоков истинного кварца способ вернуть истощенные блоки в основную сеть.
    <ItemLink id="crafting_card" /> позволяет интерфейсу запрашивать новые зарождающиеся блоки из [автокрафта](../ae2-mechanics/autocrafting.md) основной сети.