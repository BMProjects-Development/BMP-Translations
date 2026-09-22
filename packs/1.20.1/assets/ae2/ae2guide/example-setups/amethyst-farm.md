---
navigation:
  parent: example-setups/example-setups-index.md
  title: Аметистовая ферма
  icon: minecraft:amethyst_shard
---

# Выращивание аметиста
В то время как <ItemLink id="growth_accelerator" /> работает на аметисте, обычные методы фильтрации [бутонов кварца](../items-blocks-machines/budding_certus.md)
с <ItemLink id="annihilation_plane" /> не работают на аметистовых ростках. В отличие от незрелых истинных ростков, которые сбрасывают
<ItemLink id="certus_quartz_dust" />, незрелые бутоны аметиста не сбрасывают ничего, поэтому плоскость аннигиляции всегда будет разрушать их
потому что сеть никогда не может хранить "ничего".

Обойти это можно, зачаровав плоскость аннигиляции на шелковое касание. Тогда незрелые аметистовые бутоны *действительно* что-то сбрасывают
(различные стадии физических ростков) и, таким образом, могут быть отфильтрованы.

Затем <ItemLink id="minecraft:amethyst_cluster" /> должен быть снова помещен <ItemLink id="formation_plane" />, чтобы затем быть
повторно разбиты <ItemLink id="annihilation_plane" /> без шелкового касания, чтобы получить <ItemLink id="minecraft:amethyst_shard" />.

Обратите внимание, что из-за направленности кластера, прямо напротив плоскости образования должна быть сплошная поверхность блока.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/amethyst_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 1 1" max="3 2 2">
        (1) Плоскость уничтожения #1: Отсутствие графического интерфейса для настройки, но зачарованный на шелковое касание.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1 1" max="2.3 2 2">
        (2) Плоскость формирования: Фильтруется до кластера "Аметист".
        <ItemImage id="minecraft:amethyst_cluster" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 0.7 1" max="2 1 2">
        (3) Плоскость уничтожения #2: Отсутствует графический интерфейс для настройки, но может быть зачарован на удачу.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 1" max="1.3 1 2">
        (4) Шина хранения #1: Отфильтровано до осколка аметиста.
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 .7" max="1 1 1">
        (5) Шина хранения #2: Отфильтровано до Аметистового осколка. Приоритет выше, чем у основного хранилища.
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации

* Первая <ItemLink id="annihilation_plane" /> (1) не имеет графического интерфейса и не может быть настроена, но должна быть зачарована с помощью шёлкового касания.
* <ItemLink id="formation_plane" /> (2) фильтруется на <ItemLink id="minecraft:amethyst_cluster" />.
* Вторая <ItemLink id="annihilation_plane" /> (3) не имеет графического интерфейса и не может быть настроена, но может быть зачарована на удачу.
* Первая <ItemLink id="storage_bus" /> (4) фильтруется на <ItemLink id="minecraft:amethyst_shard" />.
* Вторая <ItemLink id="storage_bus" /> (5) фильтруется на <ItemLink id="minecraft:amethyst_shard" />, и имеет свой
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) установлен выше, чем у основного хранилища.

## Как это работает.

1. Первая <ItemLink id="annihilation_plane" /> пытается разрушить то, что находится перед ней, но может разрушить только <ItemLink id="minecraft:amethyst_cluster" />.
поскольку единственным хранилищем в подсети является <ItemLink id="formation_plane" />, отфильтрованный на кластер аметиста. Это работает только потому, что
плоскость зачарована на шелковое касание, иначе она могла бы ломать незрелые бутоны.
2. <ItemLink id="formation_plane" /> помещает кластер на противоположный ему блок.
3. Вторая <ItemLink id="annihilation_plane" /> разрушает кластер, создавая <ItemLink id="minecraft:amethyst_shard" />.
4. Первая <ItemLink id="storage_bus" /> хранит осколки в бочке. Технически это не нуждается в фильтрации, поскольку единственное, 
с чем должна столкнуться вторая плоскость уничтожения - это полностью выросшие кластеры.
5. Вторая <ItemLink id="storage_bus" /> предоставляет основной сети доступ ко всем аметистовым осколкам в бочке. Для нее установлен
высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority), чтобы осколки аметиста преимущественно
помещаются обратно в бочку, а не в основное хранилище.