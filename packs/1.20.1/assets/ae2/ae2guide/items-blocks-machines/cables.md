---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Кабели
  icon: fluix_glass_cable
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:white_glass_cable
- ae2:orange_glass_cable
- ae2:magenta_glass_cable
- ae2:light_blue_glass_cable
- ae2:yellow_glass_cable
- ae2:lime_glass_cable
- ae2:pink_glass_cable
- ae2:gray_glass_cable
- ae2:light_gray_glass_cable
- ae2:cyan_glass_cable
- ae2:purple_glass_cable
- ae2:blue_glass_cable
- ae2:brown_glass_cable
- ae2:green_glass_cable
- ae2:red_glass_cable
- ae2:black_glass_cable
- ae2:fluix_glass_cable
- ae2:white_covered_cable
- ae2:orange_covered_cable
- ae2:magenta_covered_cable
- ae2:light_blue_covered_cable
- ae2:yellow_covered_cable
- ae2:lime_covered_cable
- ae2:pink_covered_cable
- ae2:gray_covered_cable
- ae2:light_gray_covered_cable
- ae2:cyan_covered_cable
- ae2:purple_covered_cable
- ae2:blue_covered_cable
- ae2:brown_covered_cable
- ae2:green_covered_cable
- ae2:red_covered_cable
- ae2:black_covered_cable
- ae2:fluix_covered_cable
- ae2:white_covered_dense_cable
- ae2:orange_covered_dense_cable
- ae2:magenta_covered_dense_cable
- ae2:light_blue_covered_dense_cable
- ae2:yellow_covered_dense_cable
- ae2:lime_covered_dense_cable
- ae2:pink_covered_dense_cable
- ae2:gray_covered_dense_cable
- ae2:light_gray_covered_dense_cable
- ae2:cyan_covered_dense_cable
- ae2:purple_covered_dense_cable
- ae2:blue_covered_dense_cable
- ae2:brown_covered_dense_cable
- ae2:green_covered_dense_cable
- ae2:red_covered_dense_cable
- ae2:black_covered_dense_cable
- ae2:fluix_covered_dense_cable
- ae2:white_smart_cable
- ae2:orange_smart_cable
- ae2:magenta_smart_cable
- ae2:light_blue_smart_cable
- ae2:yellow_smart_cable
- ae2:lime_smart_cable
- ae2:pink_smart_cable
- ae2:gray_smart_cable
- ae2:light_gray_smart_cable
- ae2:cyan_smart_cable
- ae2:purple_smart_cable
- ae2:blue_smart_cable
- ae2:brown_smart_cable
- ae2:green_smart_cable
- ae2:red_smart_cable
- ae2:black_smart_cable
- ae2:fluix_smart_cable
- ae2:white_smart_dense_cable
- ae2:orange_smart_dense_cable
- ae2:magenta_smart_dense_cable
- ae2:light_blue_smart_dense_cable
- ae2:yellow_smart_dense_cable
- ae2:lime_smart_dense_cable
- ae2:pink_smart_dense_cable
- ae2:gray_smart_dense_cable
- ae2:light_gray_smart_dense_cable
- ae2:cyan_smart_dense_cable
- ae2:purple_smart_dense_cable
- ae2:blue_smart_dense_cable
- ae2:brown_smart_dense_cable
- ae2:green_smart_dense_cable
- ae2:red_smart_dense_cable
- ae2:black_smart_dense_cable
- ae2:fluix_smart_dense_cable
---

# Кабели

<GameScene zoom="3" background="transparent">
  <ImportStructure src="../assets/assemblies/cables.snbt" />
  <IsometricCamera yaw="180" pitch="30" />
</GameScene>

Хотя МЭ сети также создаются соседними машинами с поддержкой ME, кабели являются основным способом распространения сети ME на большие площади.
расширения сети ME на большие площади.

Для того чтобы соседние кабели не соединялись друг с другом, можно использовать кабели разного цвета,
что позволяет более эффективно распределять [каналы](../ae2-mechanics/channels.md). Они также влияют на цвет подключенных к ним клемм,
поэтому не обязательно, чтобы все клеммы были фиолетовыми. Изменчивые кабеля подключаются к клеммам любого другого цвета.

Примечание: **КАНАЛЫ НЕ ИМЕЮТ НИКАКОГО ОТНОШЕНИЯ К ЦВЕТУ КАБЕЛЯ**.

## Важное замечание

**Если вы новичок в AE2 и не знакомы с каналами, используйте умный кабель и плотный умный кабель везде, где только можно.
Это покажет, как каналы прокладываются через вашу сеть, и сделает их поведение более понятным.**

## Еще одно замечание.

**Это не трубы для предметов, жидкостей, энергии и т.д.** У них нет внутреннего инвентаря, поставщики шаблонов и машины не "проталкивают" в них предметы.
Все, что они делают, это соединяют AE2 [устройства](../ae2-mechanics/devices.md) вместе в сеть.

## Стеклянный кабель

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/fluix_glass_cable.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="fluix_glass_cable" /> - самый простой в изготовлении кабель, передает питание
и до 8 [каналов](../ae2-mechanics/channels.md). Он существует в 17 различных цветах,
по умолчанию - изменчивый, и может быть окрашен в любой цвет с помощью любого из 16 красителей.

Чтобы изготовить цветные кабели, соедините краситель любого типа с 8 кабелями того же типа
типа (цвет кабелей не имеет значения, но они должны быть одного типа,
стеклянные, интеллектуальные и т.д.). Вы также можете окрасить кабели с помощью любой совместимой с кузницей краски
кистью.

Окрашенный кабель можно обработать ведром воды, чтобы удалить краситель.

Вы можете покрыть кабель шерстью, чтобы создать <ItemLink id="fluix_covered_cable" />, и создать <ItemLink id="fluix_smart_cable" />, чтобы получить лучшее представление о том, что происходит с
вашими [каналами](../ae2-mechanics/channels.md).

<RecipeFor id="fluix_glass_cable" />

<RecipeFor id="blue_glass_cable" />

## Закрытый кабель

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Закрытый кабель не имеет никаких игровых преимуществ перед своим аналогом <ItemLink id="fluix_glass_cable" />. Однако его можно использовать
в качестве альтернативного эстетического варианта, если вам больше нравится закрытый вид.

Может быть окрашен так же, как и <ItemLink id="fluix_glass_cable" />. Четыре <ItemLink id="fluix_covered_cable" /> могут быть изготовлены с использованием
красного и светящегося камня, чтобы получить <ItemLink id="fluix_covered_dense_cable" />.

<Recipe id="network/cables/covered_fluix" />

<RecipeFor id="blue_covered_cable" />

## Плотный кабель

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Кабель повышенной емкости может передавать 32 канала, в отличие от стандартного кабеля, который может передавать только 8 каналов,
однако он не поддерживает шины, поэтому сначала необходимо перейти с плотного кабеля на кабель меньшего размера (например, <ItemLink id="fluix_glass_cable" /> или <ItemLink id="fluix_smart_cable" />), прежде чем использовать шины или панели.

Плотные кабели немного переопределяют поведение каналов в отношении "кратчайшего пути", каналы будут использовать кратчайший путь к
плотному кабелю, а затем по кратчайшему пути через этот плотный кабель к контроллеру.

<Recipe id="network/cables/dense_covered_fluix" />

<RecipeFor id="blue_covered_dense_cable" />

## Умный кабель

<Row>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
</Row>

Имея некоторое сходство с <ItemLink id="fluix_covered_cable" /> по внешнему виду, они выполняют диагностическую функцию, визуализируя использование каналов в кабелях.
выполняют диагностическую функцию, визуализируя использование каналов в кабелях,
каналы выглядят как светящиеся цветные линии, проходящие вдоль черной полосы на кабеле.
кабели, что позволяет понять, как используются каналы в сети.
сети. Для обычных интеллектуальных кабелей первые четыре канала отображаются в виде линий, соответствующих цвету кабеля.
Следующие четыре канала отображаются в виде линий, соответствующих цвету кабеля, а следующие четыре - в виде белых линий. В плотном интеллектуальном кабеле каждая полоса представляет собой 4 канала.

В сетях с контроллером <ItemLink id="controller" /> линии на кабелях показывают точный путь прохождения каналов.

Интеллектуальные кабели в специальных сетях вместо количества каналов, проходящих по данному конкретному кабелю, будут показывать количество каналов, используемых во всей сети.

Они также могут быть окрашены в тот же цвет, что и <ItemLink id="fluix_glass_cable" />.

<Recipe id="network/cables/smart_fluix" />

<Recipe id="network/cables/dense_smart_fluix" />

<RecipeFor id="blue_smart_cable" />
