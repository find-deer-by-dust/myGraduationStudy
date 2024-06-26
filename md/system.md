# 基于深度学习的黄金价格模拟系统的设计与实现

# 基于深度学习的黄金价格波动因素分析

# 摘要

本研究基于全球事件和黄金价格的波动，利用深度学习模型提出了一种综合分析框架和黄金价格模拟系统。通过整合传统因素数据和全球事件数据，采用长短期记忆（LSTM）模型，并利用全球事件数据集（GDELT）以及传统因素数据对黄金价格进行预测分析。在实验中，将模型分为A组和B组，A组综合考虑了传统因素数据和全球事件数据，而B组仅使用传统因素数据。实验结果表明，全球事件在黄金价格波动分析中具有显著的影响力。基于得到的模型，本文进一步开发了黄金价格模拟系统，允许用户通过多种方式上传数据进行模拟。系统具备历史记录功能，支持用户查看和使用历史数据。研究结果表明，综合考虑全球事件和传统因素数据的模型比仅使用传统因素数据的模型具有更高的预测准确性。基于本开发了一个具有一定实用价值的黄金价格模拟工具，具有一定的理论和实践意义。

关键词：黄金价格；全球事件；深度学习；长短期记忆（LSTM）；GDELT数据库；模拟系统

# Abstract

This study explores the impact of global events on gold price fluctuations and proposes an integrated analysis framework and gold price simulation system based on deep learning models. By combining traditional factor data with global event data, the Long Short-Term Memory (LSTM) model is utilized, leveraging the Global Database of Events, Language, and Tone (GDELT) alongside traditional factor data to predict gold prices. In the experiment, the model is divided into two groups: Group A, which integrates both traditional factor data and global event data, and Group B, which uses only traditional factor data. The experimental results indicate that global events significantly influence gold price fluctuations. Based on the derived model, a gold price simulation system was further developed, allowing users to upload data in various ways for simulation. The system features a historical record function, enabling users to view and use historical data. The research results demonstrate that the model considering both global events and traditional factor data achieves higher prediction accuracy compared to the model using only traditional factor data. The developed gold price simulation tool has practical value and offers insights into understanding gold price fluctuations.

Keywords: Gold price; Global events; Deep learning; Long Short-Term Memory (LSTM); GDELT database; Simulation system

# 目录

# 1 绪论

## 1.1 背景介绍

### 1.1.1 全球金融市场中黄金的重要性

黄金在全球金融市场中发挥着相当重要的作用，根据相关研究[1]，黄金的主要重要性体现在以下几个方面：

#### （1）避险资产

黄金通常会作为避险资产使用。有研究指出，当金融市场出现波动或不确定性增加时，投资者往往会转向黄金以保护其资产[2]。黄金在历史上表现出较强的稳定性决定了这一性质，尤其在金融危机期间更是如此。

#### （2）对冲通胀

黄金被认为是对抗通胀的有效工具。当货币购买力下降时，黄金的价值通常会上升，因而成为对抗通胀的有效手段。实证分析表明，黄金依然是对冲通胀的良好工具[3]。

#### （3）金融保值

理论研究证明，作为实物货币的黄金，价值稳定性是其内在的一个特征。相比会带来贬值风险的信用货币而言，在通货膨胀时期，黄金是一种具有良好效应的对冲工具。有学者研究了黄金的长期保值功能，认为黄金可以长期保持价值稳定性，并且对消费品和中间产品的实际购买力也保持稳定[4]。

综上所述，模拟黄金价格的波动具有重要意义。

### 1.1.2 传统金融研究中的局限性

#### （1）数据时间滞后性

传统金融研究通常依赖于官方发布的经济数据和统计数据，例如矿产、黄金生产、工业需求等。这些数据[3]往往具有时间滞后性，无法实时反映市场变化。此外，数据的准确性也可能受到统计方法和数据收集过程的影响，从而限制了研究结果的可靠性。

#### （2）静态分析

传统金融研究往往基于历史数据进行静态分析，忽略了市场动态变化和突发事件的影响。同时，往往使用的数据是以年或者月为单位，而黄金的价格往往是实时变动的，容易忽视绝大部分的价格波动。例如，使用的数据[5]包括道琼斯指数、美国消费价格指数、名义有效汇率、美国联邦资金利率、世界黄金储备，以上均是以年为跨度。这样的分析方法可能无法充分捕捉市场的实时波动和复杂性，从而影响预测的准确性。

## 1.2 研究目的和方式

### 1.2.1 探究事件对黄金价格的影响

研究事件涉及不同客体之间的关系，这些关系往往是具有复杂性和多维性，没有一个统一的标准去衡量。经验、直觉和理论倾向带来的影响往往会导致不同研究者对事件的看法存在差异。如果能够采用量化研究在一定程度上就可以解决此问题。从理论上讲，如果拥有了统一对所有事件进行分析的能力，就有机会和可能性去把握它们之间的关系。那么就可以得出，如果能够使用统一的测量标准对所有事件进行评估，然后将这些评估结果综合起来，就能够量化这些关系。

本项目旨在探讨事件对黄金价格的影响。但如何量化汇总全球局势的变化无疑是一个需要尝试解决的问题。随着全球化的深入和信息技术的飞速发展，大数据分析成为揭示复杂市场关系的有力工具。在这一背景下，GDELT数据库作为一个全球事件数据的宝库，通过它能够获得量化之后的全球事件数据。这为我们提供了机会，通过深度学习模型更全面地模拟全球事件与黄金价格之间的关系。利用GDELT数据库，我们可以获取全球各地的多语言、多媒体形式的全球事件数据，实现对全球事件的实时性分析，为黄金价格的波动提供另一个角度的解释。

### 1.2.2 应用深度学习模型进行多维度分析

通过使用长短期记忆网络（LSTM）模型，我们可以挖掘GDEL数据库中全球事件与黄金价格之间复杂的关联性模式，揭示潜在的趋势、周期性或突发性事件对黄金价格的影响。这些模式往往是传统非深度学习模型[6] 难以捕捉的。

如果再将全球事件数据与传统的黄金价格波动因素数据[5]（包括道琼斯指数、美国消费者价格指数、美国联邦资金利率）进行综合考虑，就能形成更为完整的分析框架，有助于更全面地理解黄金价格波动的复杂性。

### 1.2.3 模拟系统的设计与实现

设计并实现基于深度学习的黄金价格模拟系统，系统采用Streamlit框架完成前后端设计。用户可以自己输入相关数据，并利用这些数据完成对未来黄金价格的模拟分析与可视化展示。

# 2 相关技术

## 2.1 GDELT数据库介绍

GDELT（Global Database of Events, Language, and Tone）数据库是一个全球事件数据库，旨在记录和分析世界各地发生的新闻事件。其数据来源包括在线新闻文章、博客、社交媒体和广播电视新闻等。通过多语言处理技术，GDELT能够捕捉和翻译来自几乎每个国家和地区的新闻报道。

GDELT数据库的核心功能是通过自然语言处理和机器学习技术，对全球新闻事件进行结构化编码。这包括事件的时间、地点、参与者以及事件的性质等信息。此外，GDELT还记录了事件报道的情感基调，使研究人员能够分析全球情绪变化和舆论趋势[7]。

GDELT数据库在许多方面弥补了传统数据的不足。它在记录了全球范围内事件的发生时间、地点、内容和参与者信息的同时，还系统地对各类事件进行了分类以及评分[8]。

## 2.2 LSTM模型介绍

传统的神经网络（前馈神经网络，FNN）是由一系列简单的神经元构成的网络结构。其层级结构特点是每层神经元与下一层神经元全连接，但同一层的神经元之间没有连接。同时FNN的网络结构中也没有环或回路，输出与模型本身也没有反馈连接。在这种结构下，数据从输入层开始，逐层通过网络，直到输出层。因此在FNN中，所有的观测值都是独立且不相关地处理的。但是在实际使用的情况下，所处理的许多任务需要的数据中并不是没有包含大量上下文信息的数据，反而是数据之间会有复杂关联性，正如视频、音频和常见的文本数据等。因此，如果坚持使用FNN处理这些任务，就不可避免很大的局限性，这也是为何其在大规模应用中表现不佳的主要核心原因所在。

循环神经网络（Recurrent Neural Network，RNN）主要用于处理序列数据。它与 FNN 最大的不同之处便是其神经元在某一个时刻的输出是可以被作为输入，使其再一次输入到神经元的，这给他带来了能够保持数据中的依赖关系的能力。尽管 RNN 在设计之初的目的是为了学习长期的依赖性，但大量的实践[9] 表明，标准的 RNN 实际上很难实现信息的长期保存。RNN 存在梯度消失和梯度爆炸的问题，这两个问题都是由于 RNN 的迭代性引起的。总的来说，RNN 在早期也没有得到广泛的应用。

为解决长期依赖的问题，提出了长短期记忆（Long Short-Term Memory，LSTM）网络[10]，用于改进传统的循环神经网络模型。LSTM 与 RNN 并不存在在工作方式上的很大的区别或差异，但其所不同之处在于一个更加细化的内部处理单元，这是 RNN 所没有，而 LSTM 所独有的，它带来了能够有效存储与更新上下文信息的能力。LSTM 目前被广泛应用于序列学习相关的任务中，也成为了现实世界中最有效的序列模型，正是因为该优秀的性质 。

简而言之，LSTM 基本上是一个循环神经网络，能够处理长期依赖关系。例如当你在看番剧中，你可以理解发生任何情况的原因是因为你知晓之前发生的事情，RNN 也是以类似的方式工作，但其存在一个主要问题，即梯度消失问题。梯度消失指的是在训练过程中，随着时间步数的增加，梯度逐渐变得非常小，这带来了模型难以有效学习和记住长期依赖关系的问题。这限制了RNN在处理需要长期依赖的信息时的性能。因此，为了避免这个问题，LSTM 设计了一种特殊的机制，该机制让它真正地拥有了能够去利用这些长距离的时序信息的能力，例如，在故障时间序列预测方面，LSTM 具有显著的效果[11]。

# 3 基于LSTM的黄金价格模拟方法

## 3.1 数据采集与预处理

### 3.1.1 数据采集

出于数据量大小、所用设备性能和数据获取的难易程度等因素的综合考虑，本项目选择的数据时间段为2018年1月1日至2019年6月1日。

综合各数据的时间跨度和时间精度等因素的考虑，本项目最终采用以天为单位作为单一样本。即通过每天的累积的GDELT数据、每天的道琼斯指数、美国消费者价格指数、美国联邦资金利率作为该项目的特征值，而每天的黄金价格则作为对应的标签。

由于早期布雷顿森林体系的设定，美元与黄金挂钩，即1盎司黄金固定兑换35美元[12]。尽管该体系在1973年瓦解，但美元作为国际储备货币，依然保持了相对较高的稳定性。因此，在本项目中，我们采用美元作为单位来获取黄金价格，以尽可能避免因不同国家间的汇率变动对黄金价格的影响。

GDELT数据库的数据获取：

通过GDELT数据库的下载页面[8]，确定了数据链接的格式为"http://data.gdeltproject.org/gdeltv2/"+time+".export.CSV.zip"。编写Python脚本实现自动下载固定时间范围内的数据集。为提高下载效率，可采用多线程下载的方式。

![1717659619263](image/system/1717659619263.png)

黄金价格的数据获取：数据来自世界黄金协会[13]。

![1717659628076](image/system/1717659628076.png)

道琼斯指数的数据获取：数据来自英为财情[14]。

| 时间      | 美国消费者价格指数 |
| --------- | ------------------ |
| 2018/1/1  | 247.867            |
| 2018/2/1  | 248.991            |
| 2018/3/1  | 249.554            |
| 2018/4/1  | 250.546            |
| 2018/5/1  | 251.588            |
| 2018/6/1  | 251.989            |
| 2018/7/1  | 252.006            |
| 2018/8/1  | 252.146            |
| 2018/9/1  | 252.439            |
| 2018/10/1 | 252.885            |
| 2018/11/1 | 252.038            |
| 2018/12/1 | 251.233            |
| 2019/1/1  | 251.712            |
| 2019/2/1  | 252.776            |
| 2019/3/1  | 254.202            |
| 2019/4/1  | 255.548            |
| 2019/5/1  | 256.092            |
| 2019/6/1  | 256.143            |

美国消费者价格指数的数据获取：数据来自Trading Economics[15]。

| 时间       | 美国联邦资金利率 |
| ---------- | ---------------- |
| 2017/12/13 | 0.015            |
| 2018/5/20  | 0.015            |
| 2018/5/21  | 0.0175           |
| 2018/6/12  | 0.0175           |
| 2018/6/13  | 0.02             |
| 2018/9/25  | 0.02             |
| 2018/9/26  | 0.025            |
| 2018/12/18 | 0.025            |
| 2018/12/19 | 0.025            |
| 2019/7/30  | 0.025            |

美国联邦资金利率的数据获取：数据来自Trading Economics[16]。

### 3.1.2 特征提取和数据清洗

#### 3.1.2.1 GDELT库数据的筛选与清洗

GDELT 数据库包含大量特征值，每个 CSV 文件中的数据包含 58 个字段，这些字段分为以下五个部分[8]： **事件 ID 和日期属性（EVENTID AND DATE ATTRIBUTES）** 、 **参与者属性（ACTOR ATTRIBUTES）** 、 **事件行为属性（EVENT ACTION ATTRIBUTES）** 、 **事件地理信息（EVENT GEOGRAPHY）**以及**数据管理字段（DATA MANAGEMENT FIELDS）** 。

基于数据量、设备性能以及本项目的研究重点等因素的综合考虑，本项目仅选择以下特征作为输入变量：

* **B 2 Day** ：记录事件发生的日期，格式为 YYYYMMDD。
* **AD 30 QuadClass** ：该字段指定事件类型的主要分类，所有事件被划分为以下四类之一：1=口头合作，2=物质合作，3=口头冲突，4=物质冲突。
* **AE 31 GoldsteinScale** ：每个事件被分配一个介于 -10 至 +10 之间的数值，用以衡量该事件对国家可能产生的理论影响。需要注意的是，这一评分基于事件类型，而非事件的具体细节，因此小规模和大规模的同类事件将获得相同的评分 [8]。
* **AF 32 NumMentions** ：此属性值表示数据库中所有文章中提及该事件的次数。该值可用于评估事件的重要性：提及次数越多，事件可能越重要。如果事件在报道后引发了广泛讨论，该字段数值将更新（例如，一个事件在几周后可能成为舆论热点，导致大量新闻文章提及；或者在事件一周年时可能再次被广泛报道）[8]。
* **AI 35 AvgTone** ：此属性值表示所有提及该事件的文章的“语气”平均值，范围从 -100（极其消极）到 +100（极其积极）。通常的分值范围在 -10 到 +10 之间，0 表示中立。该值可用于过滤事件的“语境”，从而衡量事件的重要性及其影响。例如，轻微负面语气的暴乱可能是小事件，而极其负面语气的暴乱则表明事件可能更为严重。具有积极分值的暴乱可能表明在上下文中描述了某种积极现象（如暴力事件数量显著减少）[8]。

因为 GDELT 数据库中的数据是每15分钟记录一次，并且不会有确定的数量，因此对该数据还需要将每天中的全部15分钟的数据集继续合并，获得当天发生的所有事件数据集。但是，此时得到的数据集中每个样本实际上是对应的某一个发生的事件，而我们的需求是一个样本对应当天所发生的事件。因此，还需要对当天所有的事件进行合并。另外，LSTM 要求样本的特征数量是固定的，但每天并不会有确定数量的事件发生，因此合并后还需要对当天发生的所有事件进行筛选，确保每一天的事件数量相同。这样一来，我们就成功获得了预处理后的 GDELT 数据，其中每一个样本代表当天发生的部分事件合集，其中每个事件使用了它对应的 QuadClass、GoldsteinScale、NumMentions、AvgTone 值作为该事件的量化代表。

#### 3.1.2.2 黄金数据的处理

成功获取了1978年12月29日至2024年3月25日的黄金美元价格数据，数据来源于世界黄金协会的官方网站 [13]。利用 Python 中的 pandas 库，对获取到的每日黄金价格数据进行了预处理，更改了其中价格数值的格式。针对部分日期数据缺失的情况，采用了插值方法进行填充，确保了每一天的黄金价格数据的完整性。

#### 3.1.2.3 传统因素数据的处理

正如上文所述，这些数据并不是每天更新，甚至并不是按照一个固定的时间间隔更新，但本项目的样本是以天为单位。因此如果直接放入样本作为特征是不可靠的，因为必然会存在很多的缺失空缺。为了解决这个问题，同样采用了插值方法进行填充，确保了每一天数据的完整性。

### 3.1.3 数据的汇总

当将GDELT库数据和传统因素数据进行汇总时，可以发现尽管GDELT库数据是标准化的，但是传统因素数据不是，因此还需要对汇总后的数据统一进行归一化处理。在本项目中采用的是最小-最大标准化（MinMax Scaling）。它将数据缩放到一个固定的范围 [0, 1] ，使得数据的最小值映射到指定的最小值（0），最大值映射到指定的最大值（1）。

还需要注意到的是，当我们将以上数据缩放到 [0, 1] 中后，而黄金的价格却相较于这些数据很大，也就是标签值远大于特征值，这将会带来一系列问题，比如：

模型性能下降：标签值远大于特征值可能会导致模型对输入特征的变化不敏感，从而降低模型的性能。这是因为模型更关注标签值的变化，而不是特征值的变化。

训练不稳定：标签值远大于特征值可能会导致训练过程不稳定，例如损失函数的值可能会变得很大，导致优化过程不收敛或收敛速度非常慢。

在考虑到这种问题的情况下，本项目采用了更换黄金价格单位的方式来解决，也就是将原有的 美元/盎司 更换为 千美元/盎司。

## 3.2 模型构建与训练

### 3.2.1 实验平台

项目使用 Python 语言进行开发，并且选择了 Keras 框架来实现 LSTM 模型。具体实现环境如下表所示：

实验环境配置

| 配置              | 说明                    |
| ----------------- | ----------------------- |
| CPU               | AMD Ryzen 7 4800H       |
| GPU               | NVIDIA GeForce RTX 2060 |
| 内存              | 32GB                    |
| CUDA 版本         | 11.8                    |
| Python 版本       | 3.10.5                  |
| Transformers 版本 | 4.27.1                  |

### 3.2.2 模型的构建

本项目为了证明全球事件对黄金价格波动的影响，需要有不同方式得到的预测结果进行对照以证明全球事件确实能够对其产生影响。因此，本项目设计了两组实验，实验中的超参数等均保持相同，唯一的不同点为 A 组中每一个样本的标签为传统因素数据和 GDELT 库数据的结合，而 B 组中每一个样本的标签仅为传统因素数据。

在本项目中使用的模型一共有 3 层（两层 LSTM 和一层 Dense），而模型预测性能的评价指标是均方误差（Mean Squared Error, MSE），同时并不能忽视图像可视化带来的评价指标，因为本项目侧重于探索全球事件对黄金价格的影响，因此需要特别关注预测和实际值随时间变化和波动的相似度，并添加了辅助评价指标，平均绝对误差（Mean Absolute Error, MAE）。

### 3.2.3 模型的超参数选择

模型构建为：第一层：LSTM 层（50 个单元，返回整个序列的输出）。第二层：LSTM 层（50 个单元，只返回最后一个时间步的输出）。第三层：Dense 层（1 个单元，作为输出层）。

模型的部分其他超参数如下所示：

| 参数       | 取值                |
| ---------- | ------------------- |
| 训练集     | 70%                 |
| 验证集     | 20%                 |
| 测试集     | 10%                 |
| optimize   | adam                |
| loss       | mean_absolute_error |
| batch_size | 32                  |
| epochs     | 50                  |

## 3.3 实验结果分析与对比

### 3.3.1 实验结果

利用上文网格搜索得到的超参数对标准化后的时间序列数据训练集建立 LSTM 预测模型。通过相同超参数构建两个模型，再对两个模型进行训练和预测，最终完成了 A 和 B 两组实验，得到了两组不同的预测值结果。

### 3.3.2 数据分析

首先通过计算实际值、A 组预测值和 B 组预测值对应数组的均方误差、平均绝对误差。

可以发现的是 A 组不论是均方误差还是平均绝对误差都明显优于 B 组，这代表 A 组模型拥有更强的预测能力。

|     | 均方误差              | 平均绝对误差         |
| --- | --------------------- | -------------------- |
| A组 | 0.0001318249705946073 | 0.009479025467801125 |
| B组 | 0.02194117195904255   | 0.1479691488082592   |

### 3.3.3 可视化

通过 A 组和 B 组的预测值，可以得到两根不同的曲线，同时再添加实际值对应的曲线。本项目的重点在于对波动的分析，因此还需要关注曲线之间的波动，即趋势的联系和相似度。

![1717659589956](https://file+.vscode-resource.vscode-cdn.net/d%3A/code/system/image/system/1717659589956.png)

观察 A 组曲线，可以显著观察到对于实际值曲线有大幅度波动时，A 组曲线往往也会产生与之对应的大幅度波动情况。尤其是在2019.5.20以后的这一段预测值，能够明显看到 A 组和实际值不光数值上十分接近，在整体的波动趋势上也有着极高的相似度，这正是全球事件对价格波动影响的体现。而当实际值曲线变化幅度很小时，A 组曲线与之对应的是在一个相对很小的范围中波动。

而 B 组，其预测值已经和实际值有着不小的偏差，同时需要注意到 B 组得到的结果相较于实际值的波动性太小。这是因为 B 组中的标签值在天的刻度上有效信息内容太少，导致数据中的信息不够，使用模型很难拟合捕捉。观察 B 组的标签值也可以注意到， B 组中存在样本之间的标签完全相同，例如下图所示的2018-01-01到2018-01-31时间段内，这几个样本的标签（利率）完全相同并不存在差异，但黄金的价格却不同于这几个标签这般毫无波动。因此可以说 B 组忽略了市场 动态变化和突发事件的影响，也忽视了绝大部分的价格波动。这正是需要使用 GDELT 库中的数据的原因所在。

![1717659597509](image/system/1717659597509.png)

# 4 系统需求分析

基于上文得到的一个模型，我们可以利用其设计一个黄金价格模拟系统。需要说明的是，系统的功能是模拟而不是预测，尽管有时候模拟和预测可能会涉及到相似的数据和模型，但它们在输入方面确实有着明显的区别：

模拟通常涉及使用虚拟或人为设定的输入数据，以模拟系统或过程的行为。这些输入可能是基于假设、理论或者对系统内部关系的了解。在模拟中，我们通过观察模型的输出来理解系统在不同条件下的行为，并评估不同参数或策略对系统的影响。

而预测则通常基于真实的历史数据和已知的变量。预测模型会使用这些真实数据来推断未来事件或结果。在预测中，我们依靠过去的观察和数据模式，来估计未来可能发生的情况。预测的目的是尽可能准确地预测未来，以便为未来的决策提供支持。

## 4.1 可行性分析

系统可行性分析是一项综合考虑和评估系统各个方面的过程，旨在确定项目是否值得实施。其目的在于确认系统是否能够在规定的时间内、以最小成本解决系统搭建过程中所面临的问题。本节将从技术、经济和操作等多个方面对系统的可行性进行分析。

### 4.1.1 数据来源可行性

GDELT数据库提供了全球范围内的丰富事件数据，为研究提供了充足的材料。同时，黄金价格的历史数据和相关因素的数据也是相对易于获取的。其他因素的历史时间也都是在网络上公开透明能直接获取的。

### 4.1.2 操作可行性

系统采用B/S架构进行开发，用户通过Web浏览器访问应用程序，因此用户可以使用几乎任何支持浏览器的设备（如PC、平板电脑、手机等）来访问应用程序，而不受特定操作系统的限制。用户无需在客户端设备上安装任何额外的软件，只需一个现代的Web浏览器即可。这简化了用户的操作，降低了维护成本。应用程序的逻辑和数据都集中存储在服务器上，因此可以更容易地进行管理和维护。更新应用程序只需在服务器端进行，不需要在每个客户端设备上进行更新。由于客户端只需要一个浏览器，因此部署该系统相对来说比较容易。只需要在服务器上部署应用程序，并确保用户能够通过网络访问即可。同时，用户可以通过互联网远程访问该架构下的应用程序，无论他们身处何地。这种灵活性使得其非常适合远程工作和移动办公的需求。

总的来说，B/S架构具有操作可行性，因为它提供了跨平台兼容性、无需安装客户端软件、集中管理和维护、易于部署以及远程访问和工作等优势，使得用户可以更方便地使用和访问应用程序。

## 4.2 非功能性需求

非功能性需求分析是对软件系统的质量属性、性能、操作环境、用户体验等方面的需求进行分析和定义的过程。这些需求虽然不直接描述系统的具体功能，但对系统的整体表现和用户满意度有着重要影响[17]。

（1）可靠性
确保系统能够在预期的运行环境中长时间可靠地运行，不发生意外故障或错误。可靠性需求的核心目标是保证系统能够提供一致和预期的服务。

（2）安全性
确保软件系统和数据的机密性、完整性和可用性。安全性需求不仅要防止未经授权的访问，还要保护系统免受恶意攻击、数据泄露和其他安全威胁。

（3）可扩展性：
系统采用模块化设计，将不同功能进行了分割，这样易于系统扩展和功能开发，一旦产生新需求，可以相对较轻松容易得完成要求，同时在系统功能扩展其性能和稳定性并不有大幅度的下降。

## 4.3 功能性需求分析

黄金价格模拟系统的核心功能是通过用户所输入的数据，完成在黄金价格变化情况的模拟，并将变换情况直观地展示给用户。本系统的需求总结如下：

### 4.3.1 用户信息管理

与通常系统不一样的是，本系统并没有设立管理员和普通用户的区分，这也代表着，所有的普通用户都可以使用该系统的全部功能，并不会受到限制。但为避免系统被滥用导致性能不足以支持正常用户的使用需求，因此仍然是需要注册登录的，游客并没有访问的权限。为了实现对用户个人身份识别和验证，用户需要自己填写账号密码用以注册为普通用户。

### 4.3.2 输入数据的获取

系统拥有一共4种输入数据的方式供用户使用，有效帮助用户完成对黄金价格的模拟。

第一，用户可以在输入框中自行输入数据，实现随时就能直接模拟的功能。

第二，用户可以通过上传EXCEL文件来进行批量数据的模拟。用户将 CSV文件上传至系统，系统将分析文件中的所有数据并展示最终的模拟结果，实现了用户想要快速模拟大规模数据的请求。

第三，用户可以选择使用随机数的方式来将其作为输入数据，满足用户对模拟系统的好奇心，又不会耗费用户的时间和精力。

第四，用户可以通过查阅之前的历史输入数据，然后将其作为当前的输入数据，完成对曾经模拟操作的复现。

### 4.3.3 输入数据的处理

模型需要的标签需要数量较多，用户可能并不会输入所有的标签，而是仅仅输入部分标签。当发送这种情况时，本系统采用了使用固定值填充的方式，实现输入数据的完整化。

在模型训练时，对数据集进行了归一化的操作，提高了模型的性能，但这也代表训练时所用的数据集已不是原数据集，因此当得到了输入数据后，不能直接将输入数据放入模型内，还需要对输入数据完成一次和训练数据一样的归一化操作。

### 4.3.4 数据存储

为帮助用户更加便捷方便地查看曾经输入的数据，系统还实现了对输入数据进行持久化保存的功能。一旦用户完成输入完数据后，系统将以处理前的数据的方式存储到MySQL数据库中。用户可以随时方便地查看历史输入数据并进一步进行模拟操作。

### 4.3.5 数据模拟及可视化

系统的核心便在于实现了模拟与可视化的功能。对用户输入的单条或多条数据，系统需要利用这些数据完成对价格的模拟，并将模拟结果以可视化的方式返回给用户。

# 5 模拟系统的设计实现与测试

## 5.1 设计实现

### 5.1.1 系统体系结构设计

为了实现跨平台兼容性、无需安装客户端软件、集中管理和维护、易于部署以及远程访问和工作等功能，使用户可以更方便地使用和访问应用程序，我们使用了 B/S 体系结构来完成系统的构建。

整个系统采用了 Streamlit 框架完成了设计，其简单易用、Python原生、即时反馈、自动化组件、轻量级部署的优势和特点可以帮助我们快速构建交互式数据应用程序，提高开发效率和用户体验，

### 5.1.2 系统总体结构设计

综合考虑需要实现的功能需求、系统的安全性可靠性和可扩展性等多方面因素，最终决定将系统总体架构设计为展示层、业务层和数据持久层三个组成部分。

在展示层，完成了多个前端页面的设计，将用户使用的不同功能分放在不同的页面，避免同一页面功能繁多，影响用户的选择也回提高用户的学习和使用成本。力求让用户得到轻松简单易理解的使用体验。业务层则是围绕用户管理 、数据获取、数据模拟、可视化展示和历史记录保存等关键功能进行设计开发。在最下面的数据持久层中，选择了MySQL作为持久化数据的数据库。主要功能是将用户的信息和用户使用过程中产生的数据记录和保留下来，方便用户查阅回看。系统总体架构如下图x所示：

![1717704250668](image/system/1717704250668.png)

### 5.1.3 数据库设计

数据库在整个系统的数据管理中起到了非常重要的作用，它提供了一种统一、抽象的方式完成了数据的增删改查，无需开发者关注更底层的逻辑实现。同时其还能够有效解决数据管理中的复杂问题，提高系统的性能、可靠性和安全性，使得系统设计更加专业和完善。在基于确保数据的高效存储、管理和检索，同时保持数据的一致性、完整性和安全性等要求的综合考虑下，最终设计出的数据库中实体关系E-R图如下图x所示：

![1717704577046](image/system/1717704577046.jpg)

具体每张表的设计方案如下表所示：

用户信息表

| 序号 | 名称   | 是否为主键 | 数据类型     |
| ---- | ------ | ---------- | ------------ |
| 1    | 用户名 | 是         | varchar(100) |
| 2    | 邮箱   | 否         | varchar(100) |
| 3    | 姓名   | 否         | varchar(100) |
| 4    | 密码   | 否         | varchar(100) |

输入数据表

| 序号 | 名称     | 是否为主键 | 数据类型     |
| ---- | -------- | ---------- | ------------ |
| 1    | 数据id   | 是         | varchar(100) |
| 2    | 用户名   | 否         | varchar(100) |
| 3    | 输入数据 | 否         | LONGTEXT     |

模拟结果表

| 序号 | 名称   | 是否为主键 | 数据类型     |
| ---- | ------ | ---------- | ------------ |
| 1    | 数据id | 是         | varchar(100) |
| 2    | 模拟值 | 否         | LONGTEXT     |

### 5.1.4 系统功能模块设计与实现

系统设计成了四个功能模块：用户管理模块、数据获取模块、数据模拟模块及可视化以及历史记录模块。

用户管理模块实现了用户的注册、登录以及个人信息修改等功能。数据获取模块完成了用户多种输入数据的方式，让用户能以更方便自由的手段完成最后黄金价格的模拟。数据模拟及可视化模块完成了对用户输入的数据进行模拟，以及对模拟出来的数据的可视化实现，让用户能够以更简单更轻易的方式分析最终的模拟结果。历史记录模块实现的功能在于让用户能够查看历史数据，以及对历史数据进行使用即输入。系统功能模块图，如下图x所示：

![1717704848511](image/system/1717704848511.jpg)

#### 5.1.4.1 用户管理模块

用户管理模块是软件系统中非常重要的一部分，该模块拥有以下功能：用户注册和登录：提供新用户注册和已有用户登录的功能。验证用户身份，确保系统的安全性。用户信息管理：存储和管理用户的基本信息，如姓名、联系方式、地址等。允许用户更新和修改个人信息。密码管理：提供密码重置和修改功能。确保用户密码的安全性，通过加密存储和传输。

（1）用户注册模块，当用户第一次使用该系统时，用户首先需要成功完成账号的注册之后，才能使用账号登录系统。在页面中填写邮箱、用户名、姓名和密码点击注册便能完成整个注册过程。注册的流程图如下图x所示：

![1717705534747](image/system/1717705534747.jpg)

注册页面如下图x所示：

![1717707799857](image/system/1717707799857.png)

（2）用户登录模块，用户在完成注册后，使用注册时的用户名和密码便可完成登录，登录的流程图如下图x所示：

![1717705538325](image/system/1717705538325.jpg)

登录页面如下图x所示：

![1717708080284](image/system/1717708080284.png)

（3）忘记密码模块，当用户忘记密码时，通过输入自己的用户名就可以使用该功能重新生成一份密码用来登录自己的账号。忘记密码的流程图如下图x所示：

![1717707156753](image/system/1717707156753.jpg)

忘记密码页面如下图x所示：

![1717708426352](image/system/1717708426352.png)

（4）用户修改密码模块，当用户不满意自己旧密码时，可以通过此模块更改自己的密码。但该模块仅当用户已经成功登录后才能使用，用户首先需要输入当前的密码，当前密码输入正确后，才能完成密码的修改。修改密码的流程图如下图x所示：

![1717707465856](image/system/1717707465856.jpg)

修改密码页面如下图x所示：

![1717708691376](image/system/1717708691376.png)

#### 5.1.4.2 数据获取模块

数据获取模块的功能是获取用户输入的数据，用以后续的黄金价格模拟和结果的可视化。一共实现了三种获取数据的方式。

（1）用户直接按照输入要求将数据直接放入系统指定的文本框中，系统可以即时给出模拟结果，如下图x所示：

![1717709254235](image/system/1717709254235.png)

（2）用户可以直接导入含有数据的EXCEL文件，通过这种方式，可以让用户完成大批量数据的输入，避免了一次又一次放入文本框的繁琐，如下图x所示：

![1717721743952](image/system/1717721743952.png)

（3）如果用户不愿意输入数据，或者是第一次使用系统想要了解一下系统的功能，就可以选择使用随机数据，用户只需要输入随机生成的天数便可以完成数据的输入，如下图x所示：

![1717721908234](image/system/1717721908234.png)

#### 5.1.4.3 数据模拟及可视化模块

数据模拟及可视化模块的功能是使用用户输入的数据实现数据的模拟，将结果以可视化的方式展示出来，最后将输入数据、模拟值等数据保存到数据库中。当用户点击开始模拟后，系统便会进行数据模拟，数据模拟及可视化模块的流程图如下图x所示：

![1717722918555](image/system/1717722918555.jpg)

用户直接输入数据后完成数据模拟及可视化的结果如下图x所示：

![1717723731718](image/system/1717723731718.png)

![1717723747000](image/system/1717723747000.png)

用户导入数据后完成数据模拟及可视化的结果如下图x所示：

![1717723910469](image/system/1717723910469.png)

![1717723924623](image/system/1717723924623.png)

用户使用随机数据后完成数据模拟及可视化的结果如下图x所示：

![1717723956164](image/system/1717723956164.png)

![1717723966327](image/system/1717723966327.png)

#### 5.1.4.4 历史记录模块

该模块记录用户过去所输入的数据，为用户提供了一个查看界面。方便用户能直接回看过去输入数据后的模拟值，而不再需要重新跑一遍模型才能获得模拟值，减少了系统算力的开销，使其能够同时处理更多的用户使用该系统，实现了系统的高可用性。具体见下图x所示：

![1717723311068](image/system/1717723311068.png)

同时的用户也可以选择将历史数据得到的模拟值进行可视化展示，通过下拉选择框选择您的历史记录后，点击提交即可完成历史模拟数据的可视化。具体见下图x所示：

![1717723561121](image/system/1717723561121.png)

## 5.2 测试

### 5.2.1 测试概述

在系统完成后进行测试是至关重要的，因为测试可以帮助确保系统的质量和稳定性。以下是完成系统后进行测试的几个重要原因：

（1）验证系统功能是否按预期工作 ：测试可以验证系统是否按照规格说明书和用户需求的要求进行工作。通过测试，可以确保系统的各项功能正常运行，符合用户的预期。

（2）发现和纠正错误 ：测试可以帮助发现系统中的错误和缺陷，包括软件 bug、逻辑错误、性能问题等。通过及时发现和修复这些错误，可以提高系统的质量和稳定性，减少后期维护的成本和风险。

（3）保证系统的稳定性和可靠性 ：测试可以验证系统的稳定性和可靠性，包括系统的健壮性、容错性、并发性等方面。通过对系统进行全面的测试，可以确保系统在各种不同的情况下都能够正常运行，并且具有较高的可靠性。

（4）遵循软件开发的最佳实践 ：测试是软件开发过程中的重要环节，也是软件工程的最佳实践之一。通过测试，可以确保软件开发过程中的质量管理和控制，提高软件开发的效率和成功率。

### 5.2.2 需求测试

具体测试内容可见下表 x 所示：

| 序号 | 用户需求             | 是否达到预期 | 是否通过 |
| ---- | -------------------- | ------------ | -------- |
| 1    | 注册                 | 是           | 是       |
| 2    | 登录                 | 是           | 是       |
| 3    | 个人信息管理         | 是           | 是       |
| 4    | 直接输入数据         | 是           | 是       |
| 5    | 上传数据             | 是           | 是       |
| 6    | 随机值数据           | 是           | 是       |
| 7    | 数据模拟及可视化展示 | 是           | 是       |
| 8    | 历史数据             | 是           | 是       |

### 5.2.3 功能测试

系统功能测试是为了检查系统的功能是否符合预期。

#### 5.2.3.1 用户管理模块

用户在该模块中可以完成注册、登录等操作，经过多次的测试显示以上操作功能均可以正常实现，测试结果如下表  x 所示：

| 序号 | 测试功能名称 | 输入数据       | 预期结果       | 测试结果 |
| ---- | ------------ | -------------- | -------------- | -------- |
| 1    | 注册         | 已存在用户名   | 注册失败       | 通过     |
| 2    | 注册         | 已存在邮箱     | 注册失败       | 通过     |
| 3    | 注册         | 不一致重复密码 | 注册失败       | 通过     |
| 4    | 注册         | 不合法用户名   | 注册失败       | 通过     |
| 5    | 注册         | 正确信息       | 注册成功       | 通过     |
| 6    | 登录         | 不存在用户名   | 登录失败       | 通过     |
| 7    | 登录         | 错误密码       | 登录失败       | 通过     |
| 8    | 登录         | 正确密码       | 登录成功       | 通过     |
| 9    | 修改密码     | 新的密码       | 修改成功       | 通过     |
| 10   | 忘记密码     | 不合法的信息   | 新生成密码失败 | 通过     |

#### 5.2.3.2 数据获取

一共有三种获取的数据的方式，分别为直接输入数据、上传数据、随机值数据，测试结果如下表  x 所示：

| 序号 | 测试功能名称 | 输入数据       | 预期结果     | 测试结果 |
| :--- | ------------ | -------------- | :----------- | -------- |
| 1    | 直接输入数据 | 单条数据       | 输入成功     | 通过     |
| 2    | 直接输入数据 | 空             | 提示输入数据 | 通过     |
| 3    | 上传数据     | 正确格式       | 上传成功     | 通过     |
| 4    | 上传数据     | 错误格式       | 上传失败     | 通过     |
| 5    | 随机值数据   | 未填写天数     | 生成10天     | 通过     |
| 6    | 随机值数据   | 填写了确定天数 | 生成确定天数 | 通过     |

#### 5.2.3.3 数据模拟及可视化

该模块实现了利用输入的数据实现数据的模拟，将结果以可视化的方式展示出来，最后将输入数据、模拟值等数据保存到数据库中这些功能，测试结果如下表  x 所示：

| 序号 | 测试功能名称     | 输入数据     | 预期结果                 | 测试结果 |
| ---- | ---------------- | ------------ | ------------------------ | -------- |
| 1    | 数据模拟及可视化 | 直接输入数据 | 生成模拟数据和可视化图形 | 通过     |
| 2    | 数据模拟及可视化 | 上传数据     | 生成模拟数据和可视化图形 | 通过     |
| 3    | 数据模拟及可视化 | 随机值数据   | 生成模拟数据和可视化图形 | 通过     |

#### 5.2.3.4 历史记录模块

该模块记录用户过去所输入的数据，测试结果如下表  x 所示：

| 序号 | 测试功能名称     | 预期结果       | 测试结果 |
| ---- | ---------------- | -------------- | -------- |
| 1    | 查看历史记录     | 能看到         | 通过     |
| 2    | 使用历史记录数据 | 生成可视化图形 | 通过     |

# 结论

LSTM等机器学习模型已经广泛应用于生产生活的各个领域，GDELT数据库也在量化社会关系的研究中得到了较大规模的使用。本文提出的基于LSTM模型，使用GDELT数据库中的全球事件和传统因素数据进行综合考虑，形成更为完整的对黄金价格波动的分析框架。同时也有采取使用相同的超参数，只使用传统因素数据所构建的模型作为对比。最后基于得到的模型完成了黄金价格模拟系统，用于用户自行上传数据探索。

本文所研究的黄金价格模拟系统在为用户提供在不同于现实情况下对黄金价格的模拟服务，主要具备以下功能：第一，系统提供了多种方式让用户上传数据以进行下一步的数据模拟。用户可以通过输入单条数据的方式快速获取模拟值，但也存在用户有需要处理数据的情况，故用户也可以选择上传包含许多数据的EXCEL 文件以进行批量的模拟。用户也可以选择使用随机数据作为输入，无需再自己提供数据。第二，系统提供的历史记录功能让用户能够查看历史数据，以及对历史数据进行使用即输入。

但同样还存在一些不足和可优化之处：
（1）模型受限于设备能力和时间的约束，并没有使用GDELT数据库中的全部样本，使用样本中也没有使用其对应的全部特征。
（2）需要进一步的优化模型，提高模型推理的准确率，降低推理时间。
（3）系统还可以添加更多的功能，提高用户的使用体验。

# 参考文献

[1] 邹琼，黄金金融功能的研究[D]. 上海: 上海社会科学院, 2014.

[2] 尹力博; 柳依依，黄金是稳定的避险资产吗?——基于宏观经济不确定性的视角[J]. 国际金融研究, 2015(07).

[3] 许斌，黄金和通胀走势关系的实证分析[D]. 江苏: 江苏大学, 2010.

[4] 杨楠; 何皆易，黄金抗通胀功能的阶段性变化及影响因素分析[J]. 上海财经大学学报, 2011(06).

[5] 刘曙光; 胡再勇，黄金价格的长期决定因素稳定性分析[J]. 世界经济研究, 2008(02).

[6] 许立平; 罗明志，基于ARIMA模型的黄金价格短期分析预测[J]. 财经科学, 2011(01).

[7] 沈石; 宋长青; 程昌秀; 高剑波; 叶思菁，GDELT: 感知全球社会动态的事件大数据[J]. 世界地理研究, 2020(01).

[8] The GDELT Project. The GDELT Project, 2024年5月12日, https://www.gdeltproject.org (访问日期: 2024年5月12日).

[9] 杨丽; 吴雨茜; 王俊丽; 刘义理，循环神经网络研究综述[J]. 计算机应用, 2018(S2).

[10] Hochreiter S., Schmidhuber J. Long short-term memory[J]. Neural Computation, 1997, 9(8): 1735-1780.

[11] 王鑫; 吴际; 刘超; 杨海燕; 杜艳丽; 牛文生，基于LSTM循环神经网络的故障时间序列预测[J]. 北京航空航天大学学报, 2018(04).

[12] 布雷顿森林体系的演变与美元霸权[J]. 李向阳.世界经济与政治,2005(10)

[13] World Gold Council. Gold Price History Chart | Gold Price Trends | Goldhub, 2024年5月12日, https://china.gold.org/goldhub/data/gold-prices (访问日期: 2024年5月12日).

[14] 英为财情. 道琼斯指数历史数据, 2024年5月12日, https://cn.investing.com/indices/us-30-historical-data (访问日期: 2024年5月12日).

[15] Trading Economics. 美国 - 居民消费价格指数CPI, 2024年5月12日, https://zh.tradingeconomics.com/united-states/consumer-price-index-cpi (访问日期: 2024年5月12日).

[16] Trading Economics. 美国 - 利率, 2024年5月12日, https://zh.tradingeconomics.com/united-states/interest-rate (访问日期: 2024年5月12日).

[17]刘剑峰.面向企业的会员系统设计与实现[D].南京邮电大学,2020.DOI:10.27251/d.cnki.gnjdc.2020.001643.

# 附录

# 致谢

时间真的过得很快，特别是毕业这一年。我感觉去年找实习的时光仿佛还在昨天，转眼间我也已经快要去上班工作了。回忆这4年，我有一件这4年都没有后悔，甚至这辈子都不太可能后悔的一件事，就是在大二上开学的时候选择了转专业来到了大数据这里。

大数据专业的老师都是在很细心地教导着我们，在此对各位老师表达由衷的感谢。同样也感谢老师们在实验过程中耐心指导，有时候做的一些实验，如果只让我一人去独自完成可能真的能称得上是天方夜谭了。

也不光是学习吧，其实在其他方面老师们也是给了我们很大的支持和鼓励。纪明宇老师真的是很把我们这些同学的未来放在心上，我记得应该是开了有不下3次会吧，都是在鼓励和指导我们尽早选择未来的方向，这点真的很难得，因为在后来，我身边也会遇见很多人忙忙碌碌不知方向地度过了自己的大学时光。

同样在此尤其要感谢我的指导老师王育英老师，我这人确实是比较拖延，如果没有王育英老师不厌其烦的催促和仔细地分析，我可能也早就虚度了光阴，最终也无法完成本论文的撰写工作。在此再次感谢王育英老师。

此外我要感谢我来到东北林业大学新认识的各位朋友们，在我困难的时候与我分担痛苦，一起解决问题。

同样也要感谢我的亲人们，没有他们在背后的默默支持，我也不可能勇往直前。

最后，由于我的学术水平有限，所写论文难免有不足之处，恳请各位老师和同学提出批评和指正。
