# v1.3.2 计算化学更正与运维经验版

这一版把作者本机 2026-11 的四项计算化学更正与一批运维失败模式**脱敏**后并入公开包。属于勘误性质：v1.3.1 的 Bally–Rablen 氢基组资产是截断版本，本版已改。

## 更正（会影响结果，请升级）

- **Bally–Rablen u+1s 氢基组**：`assets/basis/Bally-H-uplus1s.gbs` 由 5s1p（截断）改为作者脚本规定的 **8s1p**（四个解收缩 6-31G s：18.7311/2.8254/0.6401/0.1613；四个紧 s：56.1934/168.580/505.741/1517.222；p=1.1）。两种资产的 J 结果不可比，旧运行的基函数计数只属于那次运行。
- **`provenance.json`**：重算并写入实际文件 sha256。旧文件里 DU4 的哈希与实际 `DU4-CHO.gbs` 不一致，已修正。
- **发表 flags**：补充 `H F H D N`（默认 SCF 与网格、`ReadAtoms/H`、`integral=nobasistransform`），并明确不要加 `SCF=XQC`、`NoSymm`、`scf=conver=10`、`grid=ultrafine`。
- **DU4 基组**：改为逐元素表（C 4-31G；N/O/F/Li/Be/B 6-31G；Si/S/P/Cl/As/Se/Br/I 3-21G*；H 8s1p），并写明 CH₂ 环境分类是化学判断、需后处理显式选定与记录理由。
- **FC 矩阵对角线**：Gaussian 耦合表对角线是磁旋比项（约 1e11），保留自配对会把 N(N−1)/2 对算成 N(N+1)/2 对；解析前先删自配对并核对对数。

## 新增

- `references/operations-lessons.md` 补 9 条运维故障：`bash -s` 遇 BOM/CRLF 的假语法错、调度器接受 GPUs 标志不等于绑定、`GAUSS_EXEDIR` 是冒号列表、`Path.write_text(newline=)` 的 Python 版本要求、PowerShell 5.1 UTF-8 往返损坏、非 ASCII 文件名的归档/传输、Cloudflare 挑战被误判成鉴权错误、按每节点空闲核数判断队列忙闲、FC 对角线陷阱。
- `references/cluster-workflow.md` 新增“先验证再承诺”（Verify access before promising it）四条。
- `references/practice-lessons.md` 与 `references/nmr-coupling.md` 同步上述科学更正。
- `docs/DESENSITIZATION.md` 增加 v1.3.2 增量与“不随包发布的内容”清单。

## 没有做

- 未上传站点专用说明（主机、队列、GPU、存储与程序路径）、真实样品案例、未发表数值或第三方正文。
- 未重跑科学验收；更正来自作者本机的实际日志与纠正记录，复现时仍需按 `practice-lessons.md` 的验收清单核对。

## 升级

```bash
python install.py --check
python install.py --host dsh --replace     # 旧版自动备份
python tools/doctor.py
```
