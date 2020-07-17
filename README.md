# 普通话语音合成前端
该实现基于python，为DurIAN/FastSpeech这类声学模型服务，因为这些模型需要预测phone的duration，所以本repo实现方法跟流行的tacotron/tacotron2的中文模型前端有点不同。

## Todo
### 一个简单的语音合成前端
- [ ] 文字转为拼音，借鉴[tacotronv2_wavernn_chinese](https://github.com/lturing/tacotronv2_wavernn_chinese)
- [ ] 因为标准拼音和[biaobei开源数据集](https://www.data-baker.com/open_source.html)中提供的对齐音素不一致，需要统计数据找出对应关系
- [ ] 在转换后的文本中去除标点符号等非音素标志，因为模型输入仅含音素
- [ ] 简单的文本标准化（借鉴[cn-text-normalizer](https://github.com/open-speech/cn-text-normalizer)）

### 一个复杂的语音合成前端
- [ ] 包含多音字预测
- [ ] 包含韵律预测
- [ ] 模型输入包含韵律，参考[DurIAN](https://arxiv.org/abs/1909.01700)
