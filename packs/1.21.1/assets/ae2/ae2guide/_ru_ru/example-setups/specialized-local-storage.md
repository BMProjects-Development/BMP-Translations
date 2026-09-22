---
navigation:
  parent: example-setups/example-setups-index.md
  title: Специализированное локальное хранение
  icon: drive
---

# Специализированное локальное хранение

Используя одно из [особых свойств интерфейса](../items-blocks-machines/interface.md#special-interactions), [подсеть](../ae2-mechanics/subnetworks.md) может представить содержимое своего хранилища основной сети, не имея возможности
видеть хранилище основной сети и занимать только 1 [канал](../ae2-mechanics/channels.md).

Это полезно для локального хранилища на какой-либо ферме, чтобы предметы не переливались в основное хранилище.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/local_storage.snbt" />

<BoxAnnotation color="#dddddd" min="4 0 0" max="5 2 1">
        (1) Некоторый метод импорта элементов (в данном случае интерфейс)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 0 0" max="4 1 1">
        (2) Дисковод: Имеет несколько ячеек. Ячейки должны быть отфильтрованы до тех, которые выдает ферма.
В ячейках могут быть карты равного распределения и карты разрушения переполнения.
        <Row><ItemImage id="item_storage_cell_4k" scale="2" /> <ItemImage id="equal_distribution_card" scale="2" /> <ItemImage id="void_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1 0" max="4 2 0.3">
        (3) Терминал крафта: Он может видеть содержимое накопителя в подсети, но не содержимое хранилища основной сети.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
        (4) Интерфейс #2: В конфигурации по умолчанию.

  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 0" max="2 1 1">
        (5) Шина хранения: Имеет более высокий приоритет, чем основное хранилище, может быть отфильтрована на все, что выдает ферма.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 0.3">
        Терминал крафта: Он может видеть содержимое хранилища основной сети *и* подсети.
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации

* Первый <ItemLink id="interface" /> (1) просто принимает предметы из любой имеющейся у вас фермы и заталкивает их в подсеть.
* В <ItemLink id="drive" /> (2) есть несколько [ячеек](../items-blocks-machines/storage_cells.md). Ячейки должны быть
  [настроенны](../items-blocks-machines/cell_workbench.md) на то, что выводит ферма.
  В ячейках могут быть <ItemLink id="equal_distribution_card" /> и <ItemLink id="void_card" />.
* Второй <ItemLink id="interface" /> (4) находится в конфигурации по умолчанию.
* Для <ItemLink id="storage_bus" /> установлен [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) выше, чем у основного хранилища. Оно может быть отфильтровано в соответствии с тем, что выдает ферма.

## Как это работает

* <ItemLink id="interface" /> в подсети показывает <ItemLink id="storage_bus" /> в основной сети содержимое <ItemLink id="drive" />.
<ItemLink id=" drive" />. Это означает, что шина хранения может напрямую извлекать элементы из ячеек накопителя и заталкивать их в ячейки.
* Для шины хранения установлен высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority), поэтому элементы будут
  помещаться обратно в подсеть, а не в основное хранилище.
* Важно отметить, что если ячейки подсети заполнятся, то предметы не будут попадать в основную сеть. Если ферма относится к типу
которая ломается при откате, то для удаления лишних элементов можно использовать <ItemLink id="void_card" />. 
* Если ферма выводит несколько элементов, то с помощью <ItemLink id="equal_distribution_card" /> можно не дать одному элементу заполнить все ячейки
и не позволять хранить другие элементы.