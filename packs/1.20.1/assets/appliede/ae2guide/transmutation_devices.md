---
navigation:
  parent: appliede-index.md
  title: Устройства трансмутации
  icon: emc_interface
  position: 10
categories:
  - appliede
item_ids:
  - appliede:emc_interface
  - appliede:cable_emc_interface
  - appliede:emc_export_bus
  - appliede:emc_import_bus
  - appliede:learning_card
---

# Устройства трансмутации

<GameScene zoom="4" background="transparent">
  <ImportStructure src="assemblies/transmutation_devices.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

В качестве дополнения к существующим <ItemLink id="ae2:interface" />, <ItemLink id="ae2:export_bus" /> и <ItemLink id="ae2:import_bus" /> из AE2, AppliedE предлагает собственные аналоги всех этих устройств, которые функционируют почти идентично оригинальным устройствам AE2 и по-прежнему работают с обычными предметами. Ключевое отличие, однако, заключается в том, что при каждой операции все предметы трансмутируются в EMC или из него.

Хотя каждое устройство может быть отфильтровано для работы с любым предметом, они смогут выполнять свою функцию только с теми предметами, которые были изучены хотя бы одним игроком, отслеживаемым <ItemLink id="appliede:emc_module">Трансмутационным модулем</ItemLink> в сети. В случае с <ItemLink id="appliede:emc_interface" />, предметы также не будут приниматься в его внутреннее хранилище для конвертации и отправки в хранилище EMC, пока они не будут предварительно изучены и известны сети. Аналогично, <ItemLink id="appliede:emc_import_bus" /> не будет втягивать предметы, которые не были изучены.

## Карта алхимического мастерства

<ItemImage id="learning_card" scale="4" />

Однако для пользователя быстро стало бы рутиной заранее изучать каждый предмет, прежде чем он сможет быть автоматически втянут в МЭ систему для превращения в EMC. По этой причине <ItemLink id="appliede:learning_card" /> можно установить в <ItemLink id="appliede:emc_interface" /> или <ItemLink id="appliede:emc_import_bus" />, чтобы они автоматически изучали поступающие предметы, при условии, что те вообще имеют значение EMC.

Обратите внимание, однако, что эти предметы будут изучены только владельцем самого устройства, т.е. игроком, который разместил шину импорта, интерфейс или сетевое устройство, отправляющее предметы в интерфейс.

## Рецепты

<Recipe id="appliede:emc_interface" />
<RecipeFor id="appliede:emc_export_bus" />
<RecipeFor id="appliede:emc_import_bus" />
<RecipeFor id="appliede:learning_card" />