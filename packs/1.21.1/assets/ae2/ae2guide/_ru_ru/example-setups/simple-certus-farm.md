---
navigation:
  parent: example-setups/example-setups-index.md
  title: Простая ферма кварца
  icon: certus_quartz_crystal
  position: 110
---

# Простая ферма кварца

Как уже упоминалось в [Выращивании кварца](../ae2-mechanics/certus-growth.md), автоматизация <ItemLink id="certus_quartz_crystal" /> заключается в том, что для сбора <ItemLink id="annihilation_plane" /> и <ItemLink id="storage_bus" />
участвуют <ItemLink id="annihilation_plane" /> и <ItemLink id="storage_bus" />. 

<ItemLink id="growth_accelerator" /> с помощью <ItemLink id="growth_accelerator" /> ускоряют рост ростков истинного кварца, а затем плоскости
разбивают полностью выросшие <ItemLink id="quartz_cluster" />. Для их фильтрации используется подозрительно удачная особенность, заключающаяся в том, что незрелые бутоны кварца сбрасывают <ItemLink id="quartz_cluster" />.
Бутоны истинного кварца сбрасывают <ItemLink id="certus_quartz_dust" />, а затем ничего не производят.

Эта ферма работает полностью автоматически с <ItemLink id="flawless_budding_quartz" />, но потресканные, осколочные и поврежденные типы
кварца придется заменять вручную. Или, как описано в [Полу-автоматической ферме кварца](semiauto-certus-farm.md)
и [Улучшенной ферме кварца](advanced-certus-farm.md), автоматически.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/simple_certus_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="3.7 1 1" max="4 2 2">
        (1) Плоскость уничтожения: Не имеет графического интерфейса для настройки, но может быть зачарована на удачу.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="3.3 2 2">
        (2) Шина хранения #1: Фильтруется на кристалл истинного кварца.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 .7" max="2 2 1">
        (3) Шина хранения #2: Фильтруется на кристалл истинного кварца. Имеет более высокий приоритет, чем основное хранилище.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации

* Первая <ItemLink id="annihilation_plane" /> (1) не имеет графического интерфейса и не может быть настроена, но может быть зачарована на удачу.
* Первая <ItemLink id="storage_bus" /> (2) фильтруется на <ItemLink id="certus_quartz_crystal" />.
* Вторая <ItemLink id="storage_bus" /> (3) отфильтрована на <ItemLink id="certus_quartz_crystal" /> и имеет свой
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) установлен выше, чем у основного хранилища.

## Как это работает

1. <ItemLink id="annihilation_plane" /> пытается сломать то, что находится перед ним, но может сломать только <ItemLink id="quartz_cluster" />,
   поскольку единственным хранилищем в подсети является <ItemLink id="storage_bus" />, отфильтрованный на <ItemLink id="certus_quartz_crystal" />.
4. В первой <ItemLink id="storage_bus" /> хранятся кристаллы истинного кварца в бочке.
5. Вторая <ItemLink id="storage_bus" /> предоставляет основной сети доступ ко всем кристаллам, находящимся в бочке. Для него установлен
   высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority), чтобы кристаллы кварца 
помещались обратно в бочку, а не в основное хранилище.
