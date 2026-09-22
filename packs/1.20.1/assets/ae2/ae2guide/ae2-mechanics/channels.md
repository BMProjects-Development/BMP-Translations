---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: Каналы
  icon: controller
---

# Каналы

Applied Energistics 2 [МЭ сеть](me-network-connections.md) требует
каналы для поддержки [устройств](../ae2-mechanics/devices.md) используются сетевые хранилища или другие сетевые
сервисы. Рассматривайте каналы как USB-кабели для всех ваших устройств. Компьютер имеет лишь ограниченное количество портов USB и может поддерживать лишь
определенное количество подключенных к нему устройств. Большинство механизмов, полноблочных устройств и стандартных кабелей могут пропускать
не более 8 каналов. Полноблочные устройства и стандартные кабели можно представить как связку из 8 "канальных проводов". Однако, [плотный кабель](../items-blocks-machines/cables.md#dense-cable) может поддерживать
до 32 каналов. Единственными устройствами, способными передавать 32 канала, являются <ItemLink id="me_p2p_tunnel" />
и [Квантовый мост](../items-blocks-machines/quantum_bridge.md). Каждый раз, когда устройство использует канал, представьте себе, что оно выдергивает usb-"провод" из
из связки, что, очевидно, означает, что этот "провод" не будет доступен далее по линии.

<GameScene zoom="7" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_demonstration_1.snbt" />

  <LineAnnotation color="#33ff33" from="1 .4 .7" to="2.4 .4 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .7" to="2.4 .6 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .6" to="2.6 .4 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.4 .6 .7" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .4 .7" to="2.4 .4 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .6 .6" to="2.6 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 .6" to="2.6 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.1 .6 1.5" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 1.5" to="2.9 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.6 .6 1.5" to="2.6 .9 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .1 1.5" to="2.4 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .4" to="3.5 .6 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="3.5 .6 .4" to="3.5 .9 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="3.5 .1 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .3" to="1.5 .6 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1.5 .6 .3" to="1.5 .9 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1.5 .1 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#ff3333" from="3.5 .5 .5" to="5.5 .5 .5" alwaysOnTop={true}>
  Все 8 каналов используются, поэтому дисководу не достается ни одного.  
  </LineAnnotation>

  <LineAnnotation color="#993333" from="1 .5 .5" to="1.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="1.5 .5 .5" to="1.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2 .5 .5" to="2.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2.5 .5 .5" to="2.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="3 .5 .5" to="3.25 .5 .5" alwaysOnTop={true}/>

  <DiamondAnnotation pos="3.6 0.5 0.5" color="#ff0000">
        Все 8 каналов в кабеле были использованы, поэтому дисковод не получает ни одного.
    </DiamondAnnotation>

  <IsometricCamera yaw="15" pitch="30" />
</GameScene>

Простой способ увидеть, как используются и маршрутизируются каналы в вашей сети, - это использовать [умные кабеля](../items-blocks-machines/cables.md), которые будут отображать на них пути и использование каналов.

Каналы потребляют 1⁄128 аэ/т на каждый узел, который они пересекают, это означает, что при
добавлении <ItemLink id="controller" /> для
сети с 8 устройствами и более 96 узлами ваше использование мощности может фактически
снизить потребление энергии, поскольку изменяется способ распределения каналов.

Следует отметить, что **КАНАЛЫ НЕ ИМЕЮТ НИКАКОГО ОТНОШЕНИЯ К ЦВЕТУ КАБЕЛЯ**, все, что делает цвет кабеля, - это делает кабель несоединимым.

## Маршрутизация каналов

При использовании <ItemLink id="controller" />,
каналы прокладывают маршрут в три этапа. Сначала они выбирают кратчайший путь через соседние механизмы к ближайшему [обыному кабелю](../items-blocks-machines/cables.md)
(стеклянные, закрытые или умные). Затем они проходят кратчайший путь по этому обычному кабелю до ближайшего [плотного кабеля](../items-blocks-machines/cables.md)
(плотный или плотный умный). TЗатем они проходят по кратчайшему пути через этот плотный кабель к <ItemLink id="controller" />.
Если кратчайший путь уже максимален, то некоторые [устройства](devices.md) могут не получить нужные каналы, используйте
цветные кабели, кабельные якоря и туннели для того, чтобы каналы шли по желаемому пути

Например, в этом случае некоторые диски не получают каналы, поскольку, несмотря на достаточную емкость кабелей, каналы пытаются пройти по кратчайшему пути, перегружая одни кабели и 
оставляя другие пустыми.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 3.6" to="1.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.4 0.5 3.6" to="1.4 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 1.6" to="0.6 .5 1.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 1.6" to="0.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 3.4" to="1.4 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 3.4" to="1.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <BoxAnnotation color="#dddddd" min="1.2 0.2 3.2" max="1.8 0.8 3.8" alwaysOnTop={true} thickness="0.05">
        Здесь пытаются пройти более 8 каналов, поэтому некоторые из них отсекаются.
  </BoxAnnotation>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

Это можно исправить, если более тщательно ограничить пути прохождения каналов. Сети должны быть древовидными (или кустовидными).
Петли и неоднозначные пути каналов должны быть сведены к минимуму.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue_fix.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 5.6" to="1 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

## Специальные сети

Сеть без <ItemLink id="controller" />
считается специальной и может поддерживать до 8 устройств, использующих канал.
При превышении 8 устройств использующие канал устройства сети будут отключены,
Вы можете либо удалить устройства, либо добавить <ItemLink id="controller" />.

В отличие от сетей с контроллером, [умные кабели](../items-blocks-machines/cables.md) в специальных сетях будут отображать количество
каналов, используемых во всей сети, а не количество каналов, проходящих через данный конкретный кабель.

При использовании данных сетей
каждое устройство использует 1 канал в сети, что сильно отличается от того, как <ItemLink id="controller" /> распределяет каналы на основе
кратчайшего маршрута.

## Дизайн

Как уже отмечалось в [маршрутизации каналов](channels.md#channel-routing), лучше всего проектировать сеть в виде дерева, где плотные кабели ответвляются от контроллера, 
обычные кабели ответвляются от плотных,  кластерах по 8 и менее штук на обычных кабелях.

Вот пример того, чего делать не следует:

Следование по путям каналов,

1. Сразу после выхода из контроллера справа мы имеем узкое место в 8 каналов, поскольку дисковод работает как обычный кабель.
Однако поскольку мы не используем здесь умный кабель, мы не можем видеть, сколько каналов используется. Осталось 8 каналов.
2. Дисковод забирает один канал.
Осталось 7 каналов.
3. 2 канала выходят на терминалы.
Осталось 5 каналов.
4. Продолжая движение вправо, интерфейс захватывает еще один канал.
Осталось 4 канала.
5. 1 канал поднимается к МЭ интерфейсу.
Осталось 3 канала.
6. Продолжая движение вправо, 1 канал поднимается на шину импорта.
Остается 2 канала.
7. Источник шаблонов, питающий сборщики, получает только 2 канала, поэтому 2 интерфейса не получают каналов.

В конечном счете, ошибка заключается в том, что мы не продумали, как будут распределяться каналы.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/bad_network_structure.snbt" />

<LineAnnotation color="#33ff33" from="6.5 .5 1.5" to="6 .5 1.5" alwaysOnTop={true} thickness="0.4">
  32 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="6 .5 1.5" to="5.5 .5 1.5" alwaysOnTop={true} thickness="0.2">
  8 каналов
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 1.5 1.5" alwaysOnTop={true} thickness="0.1">
  2 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 1.5 1.5" to="5.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 2.5 1.5" to="5.5 2.5 1.1" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="4.5 .5 1.5" alwaysOnTop={true} thickness="0.158">
  5 каналов
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 1.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="3.5 .5 1.5" alwaysOnTop={true} thickness="0.122">
  3 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="3.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 2.5 1.5" to="3.7 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="1.5 .5 1.5" alwaysOnTop={true} thickness="0.1">
  2 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="1.5 0.3 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="0.5 0.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="0.5 0.5 1.5" to="0.5 0.5 0.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#ff3333" from="0.5 1.5 1.5" to="0.5 1.3 1.5" alwaysOnTop={true} thickness="0.071">
  Нет каналов
</LineAnnotation>

<LineAnnotation color="#ff3333" from="1.5 1.5 0.5" to="1.5 1.3 0.5" alwaysOnTop={true} thickness="0.071">
   Нет каналов
</LineAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

---

Вот пример хорошей структуры:

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="6.9 0 4.9" max="9.1 4 7.1" thickness="0.05">
        Обратите внимание, что интерфейсы расположены в отдельных группах по 8 штук.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 4 4" max="8 5 5" thickness="0.05">
        Два обычных кабеля с большим количеством каналов, сходящихся вместе, означают, что вам нужен плотный кабель.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 0 13" max="8 1 14" thickness="0.05">
        Разные цвета кабелей используются для предотвращения соединения соседних кабелей.
    </BoxAnnotation>


  <IsometricCamera yaw="315" pitch="30" />
</GameScene>

## Режимы каналов

В AE2 10.0.0 для Minecraft 1.18 появились новые опции, позволяющие изменить поведение каналов AE2 в вашем мире.
В общей секции (`каналы`) появилась новая опция конфигурации, которая управляет этой опцией, а также новая внутриигровая
команда для операторов, позволяющая изменять режим и конфигурацию изнутри игры. Команда выглядит так: `/ae2 channelmode <mode>`
для изменения режима и `/ae2 channelmode` для отображения текущего режима. При изменении режима в игре все существующие сетки
перезагрузятся и немедленно перейдут в новый режим.

Это воскрешает и улучшает опцию, которая была доступна в Minecraft 1.12, и предоставляет лучшие возможности для
игроков, которые просто хотят более спокойного геймплея, но не хотят, чтобы механика была удалена полностью.

В следующей таблице перечислены режимы, доступные как в конфигурационном файле, так и в команде.

| Настройки     | Описание                                                                                                                                                                                                                                                                         |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `по умолчанию | Стандартный режим с канальной емкостью кабельных и спец. сетей, описанный на данном сайте                                                                                                                                                                                        |
| `x2`          | Пропускная способность всех каналов удваивается (16 в обычном кабеле, 64 в плотном кабеле, специальные сети поддерживают 16 каналов)                                                                                                                                             |
| `x3`          | Все каналы увеличиваются в три раза (24 в обычном кабеле, 92 в плотном кабеле, специальные сети поддерживают 24 канала)                                                                                                                                                          |
| `x4`          | Все каналы увеличиваются в четыре раза (32 в обычном кабеле, 128 в плотном кабеле, специальные сети поддерживают 32 канала)                                                                                                                                                      |
| `бесконечный  | Сняты все ограничения на количество каналов. Контроллеры по-прежнему *значительно* снижают энергопотребление сетей. Умные кабели будут переключаться только между полностью выключенными (ни один канал не передается) и полностью включенными (передается 1 или более каналов). |