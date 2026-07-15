# Study Plan — Engenharia de Software para IA e Frameworks Profundos

**Course:** Engenharia de Software para IA e Frameworks Profundos
**Instructor:** Fernando Maciano de Paula Neto (fernando@cin.ufpe.br)
**Workload:** 32h · Group project (6–7 pessoas, 6 entregas + apresentação final)
**Today:** 2026-06-13 (first class — Aula 1)
**Final presentation:** 2026-12-09

---

## How to use this plan

For each class, you have **three layers**:
1. **Pre-class (3–5h)** — read + watch one canonical resource and warm up with 1 mini-exercise.
2. **Post-class (4–8h)** — deeper drills + quiz + apply to your project deliverable.
3. **Stretch (optional)** — book chapters / papers if you want to go beyond.

**Cadence rule:** finish post-class within 72h of the lecture, while it's still warm. The deliverable is due before the *next* class.

---

## Class-by-class roadmap

### Aula 0 (already-released) — Anaconda + Curso

- **Goal:** environment ready, syllabus understood.
- **Do this once, today:**
  - Install Anaconda + create env: `conda create -n eng-ia python=3.11 numpy pandas matplotlib pytorch jupyter pytest mypy black ruff -c pytorch`
  - Verify: `python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"` (Mac) or `torch.cuda.is_available()` (Linux/Win).
  - Set up VS Code with: Python, Pylance, Jupyter, GitLens, Ruff extensions.
  - Create a private GitHub repo for the project; add team as collaborators.

---

### Aula 1 — 2026-06-13 (8h–11h45) — Funções, Modularização, Tipagem, Numpy
**Entrega 1 starts.**

#### Topics
- Funções (parâmetros default, *args/**kwargs, escopo, closures)
- Modularização (módulos, packages, `__init__.py`, imports)
- Tipagem estática (type hints, `typing`, `mypy`)
- NumPy: ndarray, broadcasting, vectorization, álgebra linear

#### Pre-class (do today before 8h, ~3h)
- 📖 **Think Python (Downey)** — Cap. 3 (Functions), Cap. 6 (Fruitful Functions), Cap. 14 (Files & modules). Free at https://greenteapress.com/wp/think-python-3e/
- 📺 **mCoding — "Python Type Hints"** (YouTube, ~15 min) — https://www.youtube.com/@mCoding
- 📖 **NumPy Quickstart** — https://numpy.org/doc/stable/user/quickstart.html

#### Post-class (~6h, finish by 16/06)
- 🧪 **NumPy 100 exercises** (do 1–40) — https://github.com/rougier/numpy-100
- 🧪 **mypy strict mode** — type-annotate one file from your project; run `mypy --strict`.
- 📺 **ArjanCodes — "Cohesion and Coupling"** (~15 min)
- ✅ Self-quiz below.

#### Self-quiz (Aula 1)
1. What's the difference between `def f(x, lst=[])` and `def f(x, lst=None)`? Why does the first form bite you?
2. Explain broadcasting: `a.shape = (3, 1)`, `b.shape = (1, 4)` — what's `(a+b).shape`?
3. Why is `np.dot(A, B)` typically faster than a Python `for` loop computing the same thing?
4. What does `from .utils import foo` mean and when does it fail?
5. Given `def add(a: int, b: int) -> int`, why doesn't Python *enforce* the types at runtime? What does mypy give you that the interpreter doesn't?
6. What's the difference between `np.array([1,2,3])` (dtype int64) and `np.array([1,2,3], dtype=np.float32)` for a deep-learning workflow?
7. Refactor: take a 30-line `main.py` notebook script and split into `data.py`, `model.py`, `train.py`, `__init__.py`. What goes where?

#### Entrega 1 — typical scope
- Module structure of the project repo (`src/`, `tests/`, `notebooks/`, `pyproject.toml`).
- One vectorized NumPy routine (e.g. data preprocessing) with type hints + docstrings.

---

### Aula 2 — 2026-06-20 (8h–11h45) — Introdução ao PyTorch (parte 1)
**Entrega 2 starts.**

#### Topics
- Tensors (criação, dtype, device, ops básicas)
- Autograd (computational graph, `requires_grad`, `.backward()`)
- nn.Module + nn.Sequential
- Loss functions, optimizers básicos (SGD, Adam)

#### Pre-class (~4h, done by 19/06)
- 📖 **Deep Learning with PyTorch (Stevens et al.)** — Cap. 3 (Tensors), Cap. 4 (Real-world data → tensors). Free PDF: https://www.manning.com/books/deep-learning-with-pytorch (search "free ebook").
- 📺 **PyTorch official "60-Minute Blitz"** — https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html — *do all 4 tutorials*.
- 📺 **Andrej Karpathy — "Neural Networks: Zero to Hero — micrograd"** (Lecture 1, ~2h) — https://www.youtube.com/@AndrejKarpathy. This makes autograd click.

#### Post-class (~6h)
- 🧪 **PyTorch examples repo** — train MLP on MNIST from scratch: https://github.com/pytorch/examples/tree/main/mnist
- 🧪 Write your own `nn.Module` with custom `forward` (no `nn.Sequential`).
- 🧪 Recreate one autograd example by hand, then check with `.backward()`.
- ✅ Self-quiz below.

#### Self-quiz (Aula 2)
1. What does `tensor.requires_grad = True` do? When is the gradient actually computed?
2. Why must you call `optimizer.zero_grad()` before `.backward()`? What happens if you forget?
3. Compare `torch.tensor([1,2,3])` vs `torch.Tensor([1,2,3])` — what's different and why does it matter?
4. What's `with torch.no_grad():` for? Give two scenarios where you'd use it.
5. `model.train()` vs `model.eval()` — what behaviors actually change?
6. Given a 2-layer MLP with ReLU, write the forward pass in raw PyTorch ops (no `nn.Linear`).
7. Explain `.detach()` vs `.clone()` vs `.cpu()`.

#### Entrega 2 — typical scope
- Baseline PyTorch model defined as `nn.Module`, trains end-to-end on a small dataset.

---

### Aula 3 — 2026-07-24 (18h15–22h30) — Python: Testes (Unittest)
**Entrega 4 starts** (note: spreadsheet shows non-sequential delivery numbers — confirm with prof).

#### Topics
- `unittest` + `pytest` basics
- AAA pattern (Arrange / Act / Assert)
- Fixtures, parametrize, mocks
- Test coverage (`coverage.py`)
- Testing ML code (deterministic seeds, tensor equality, golden tests)

#### Pre-class (~4h)
- 📖 **Real Python — "Getting Started With Testing in Python"** — https://realpython.com/python-testing/
- 📖 **pytest docs — Quickstart** — https://docs.pytest.org/en/stable/getting-started.html
- 📺 **ArjanCodes — "How to Write Awesome Unit Tests"** (~20 min)
- 📖 **"How to Trust Your Deep Learning Code"** (Krzysztof Chrobak) — Google it; great article on ML-specific testing.

#### Post-class (~5h)
- 🧪 Write 10 tests for an existing module: 5 happy-path, 3 edge cases, 2 failure modes.
- 🧪 Add `pytest --cov=src` to your project; aim for ≥70% coverage on non-training code.
- 🧪 Property-based testing — try `hypothesis` for one numerical function.
- 🧪 ML-specific: write a test that checks `model(x).shape` and one that asserts the loss decreases after one optim step on a tiny synthetic batch.

#### Self-quiz (Aula 3)
1. What's the difference between a unit test and an integration test? Give an example of each from an ML pipeline.
2. Why is `assertAlmostEqual` (or `torch.testing.assert_close`) needed for floating-point assertions?
3. What's a fixture? Show how `@pytest.fixture` differs from `setUp` in unittest.
4. How do you make a test deterministic when it depends on `torch.randn`?
5. What's a flaky test? Give two common causes in ML code.
6. `mock.patch` — when do you use it vs just passing a stub object?
7. What does `coverage` *not* tell you about your test suite's quality?

---

### Aula 4 — 2026-08-08 (13h30–17h30) — Engenharia de Software: Intro + Requisitos
**Entrega 5 starts.**

#### Topics
- O que é engenharia de software (vs "só programar")
- Ciclo de vida (waterfall, agile, kanban)
- Levantamento de requisitos (funcionais, não-funcionais)
- User stories, casos de uso
- Especificação para projetos de IA (SLOs, métricas, dataset reqs)

#### Pre-class (~3h)
- 📖 **Pragmatic Programmer (Hunt & Thomas)** — Cap. 1 ("A Pragmatic Philosophy") + Cap. 2 ("A Pragmatic Approach"). Skim if no time.
- 📖 **"Hidden Technical Debt in Machine Learning Systems" (Sculley et al., NeurIPS 2014)** — https://papers.nips.cc/paper/2014/hash/86df7dcfd896fcaf2674f757a2463eba — required reading. Short and devastating.
- 📺 **ThoughtWorks — "Continuous Delivery for ML (CD4ML)"** (~30 min)

#### Post-class (~4h)
- 🧪 Write the **PRD** for your project: problem, users, functional reqs, non-functional reqs (latency, accuracy target, dataset size), out-of-scope.
- 🧪 Translate 5 reqs into user stories (`As a <X>, I want <Y>, so that <Z>`).
- 🧪 Define **3 acceptance metrics** for your model (e.g., F1 ≥ 0.85, p95 inference < 200ms, training reproducible from seed).

#### Self-quiz (Aula 4)
1. Functional vs non-functional req — give two of each for a "spam classifier" service.
2. What's a "definition of done" and why does it matter for ML projects (where "done" is fuzzier)?
3. Sculley et al. list "CACE" — Changing Anything Changes Everything. Why is this worse in ML than in regular software?
4. What's the difference between a *user story* and a *use case*?
5. Your stakeholder says "I want it to be accurate." Rewrite this as a measurable requirement.

---

### Aula 5 — 2026-08-21 (18h15–22h30) — ES: Design & Arquitetura + Git
**Entrega 6 starts.**

#### Topics
- Princípios SOLID
- Design patterns relevantes (Strategy, Factory, Adapter)
- Arquitetura em camadas / hexagonal para ML pipelines
- Git: branches, merge vs rebase, conflitos, tags, gitflow vs trunk-based
- Code review, PR etiquette

#### Pre-class (~5h)
- 📖 **Clean Code (Martin)** — Cap. 2 (Names), Cap. 3 (Functions), Cap. 10 (Classes).
- 📖 **Pro Git (Chacon & Straub)** — Cap. 2 (Basics) + Cap. 3 (Branching). Free: https://git-scm.com/book
- 📺 **ArjanCodes — "SOLID Principles" series** (5 vídeos curtos)
- 🧪 **Learn Git Branching** (interactive) — https://learngitbranching.js.org/ — do all "Main" + "Remote" levels.

#### Post-class (~5h)
- 🧪 Refactor one module from your project applying at least 2 SOLID principles. Document the before/after in the PR description.
- 🧪 Set up a `pre-commit` config: black + ruff + mypy + pytest on changed files. https://pre-commit.com/
- 🧪 Practice rebase: `git rebase -i HEAD~5` to squash; `git rebase main` on a feature branch.
- 🧪 Open at least one PR per teammate and do a real review.

#### Self-quiz (Aula 5)
1. Explain SRP with an ML example (think `DataLoader`, `Trainer`, `Logger`).
2. Open/Closed: how would you design a model registry that supports adding new model types without editing existing code?
3. `git merge` vs `git rebase` — when does each lose information?
4. You've committed a 500MB checkpoint to git. How do you fully remove it from history?
5. What does `git reset --soft HEAD~1` vs `--hard HEAD~1` do?
6. Trunk-based dev vs gitflow — which fits a 7-person student project better and why?
7. Conflict during rebase on file `train.py` — walk through the resolution.

---

### Aula 6 — 2026-08-29 (8h–11h45) — Exercícios + Acompanhamento

- **Bring:** working repo, blocked items, deliverables 1–6 status.
- **Use the prof's office hours.** This is the cheapest senior-engineer feedback you'll get all semester.
- **Internal team retro:** what's slow? What's blocked? Who needs to swap tasks?

---

### Aula 7 — 2026-11-07 (13h30–17h30) — Introdução ao PyTorch (parte 2)
**Entrega 3** (yes — non-sequential per spreadsheet).

#### Topics (likely — confirm with prof)
- Custom `Dataset` + `DataLoader`
- Training loops at scale (gradient clipping, scheduling, mixed precision)
- Saving/loading checkpoints
- TensorBoard / Weights & Biases
- (Possibly) distributed training (`DDP`)

#### Pre-class (~6h)
- 📖 **Deep Learning with PyTorch (Stevens)** — Cap. 7–9 (real datasets, training loops).
- 📺 **PyTorch — "Training a Classifier"** + **"Optimization"** + **"Save & Load Model"** — https://pytorch.org/tutorials/beginner/basics/intro.html
- 📺 **Karpathy — "Building makemore"** parts 2–4 (MLP/optim deep-dive).
- 📖 **"A Recipe for Training Neural Networks" (Karpathy blog)** — https://karpathy.github.io/2019/04/25/recipe/ — the single best ML-engineering essay.

#### Post-class (~6h)
- 🧪 Refactor your project to use `Dataset` + `DataLoader` with a custom transform pipeline.
- 🧪 Add checkpointing (save best by val loss; resume from checkpoint).
- 🧪 Add TensorBoard logging for loss + at least one metric + one image/embedding.
- 🧪 Profile one training step with `torch.profiler` and identify the bottleneck.

#### Self-quiz (Aula 7)
1. Why subclass `Dataset` instead of just using a list of tuples?
2. `num_workers > 0` — what wins, what breaks?
3. Save `model.state_dict()` vs `torch.save(model)` — which and why?
4. Mixed precision — what's `autocast` doing? When does it hurt?
5. Why do training curves look smooth in TB but accuracy stalls? What might explain it?
6. Karpathy's "recipe": list the steps before you start tuning hyperparameters.

---

### Aula 8 — 2026-12-09 (8h–11h45) — Apresentação Final

#### Two weeks before
- Freeze code (tag `v1.0`).
- README com: problema, dataset, modelo, métricas, como rodar, limitações.
- Slide deck (≤10 slides for a 10-min talk):
  1. Problem & users
  2. Data
  3. Architecture (system + model)
  4. Engineering practices used (tests, CI, modularização) — **this is the rubric**
  5. Results (with at least one ablation or comparison)
  6. Limitações & next steps
- Rehearse twice with timer. Cut by 30%. Rehearse again.

#### Day-of checklist
- Repo público (ou shared com prof).
- Demo gravada como fallback (se a internet falhar).
- Quem fala o quê — todo mundo apresenta um pedaço.

---

## Project deliverables — running checklist

| # | Starts | Theme | Suggested artifact |
|---|--------|-------|--------------------|
| 1 | 13/06 | Modularização + tipagem + NumPy | Repo skeleton, `pyproject.toml`, typed data-loading module |
| 2 | 20/06 | PyTorch básico | Baseline `nn.Module` training on toy dataset |
| 3 | 07/11 | PyTorch avançado | Custom Dataset, full training loop, checkpointing, TB |
| 4 | 24/07 | Testes | `pytest` suite, ≥70% coverage on non-training code |
| 5 | 08/08 | Requisitos / ES intro | PRD + acceptance metrics + risk log |
| 6 | 21/08 | Design + Git | Refactor with SOLID, PR template, branch protection |

---

## Curated resources (one-stop reference)

### Books (priority order)
1. **Deep Learning with PyTorch** (Stevens, Antiga, Viehmann) — 80% of the PyTorch content of this course.
2. **Clean Code** (Martin) — read Caps 1–4, 9–10.
3. **Pro Git** (Chacon, Straub) — free online, treat as reference.
4. **Pragmatic Programmer** (Hunt, Thomas) — short, dense, life-changing.
5. **Think Python 3e** (Downey) — only if you're rusty on Python basics.

### Free courses to watch alongside
- **Karpathy — Neural Networks: Zero to Hero** (YouTube). The single best PyTorch+DL tutorial in existence.
- **Full Stack Deep Learning** — https://fullstackdeeplearning.com/ — engineering-flavored ML.
- **MIT 6.S191 Introduction to Deep Learning** — https://introtodeeplearning.com/

### Practice / drill platforms
- **NumPy 100** — https://github.com/rougier/numpy-100
- **PyTorch examples** — https://github.com/pytorch/examples
- **Learn Git Branching** — https://learngitbranching.js.org/
- **Exercism — Python track** — https://exercism.org/tracks/python (great for typing + functions)

### Reference docs (bookmark these)
- PyTorch — https://pytorch.org/docs
- NumPy — https://numpy.org/doc
- Python — https://docs.python.org
- pytest — https://docs.pytest.org
- Git — https://git-scm.com/doc

### Essays to read once
- Karpathy — *A Recipe for Training Neural Networks* (https://karpathy.github.io/2019/04/25/recipe/)
- Sculley et al. — *Hidden Technical Debt in Machine Learning Systems*
- Joel Spolsky — *The Joel Test* (still gold for evaluating dev practices)

---

## Weekly cadence (suggested template)

| Day | Block | What |
|-----|-------|------|
| Sat (post-class) | 2h | Review notes, do self-quiz |
| Sun | 3h | Drills (NumPy 100 / pytest / Git branching) |
| Mon–Wed | 1h × 3 | Project deliverable work |
| Thu | 2h | Pair w/ teammate (PR review or pairing) |
| Fri | 1h | Read 1 essay or book chapter for next class |

**Total ~12h/week.** Adjust to your reality, but anything below 6h/week and the deliverables will start slipping.

---

## Excellence multipliers (cheap, high-leverage)

1. **Open a PR for every change ≥10 lines.** Even solo. Forces self-review.
2. **`pre-commit` from day 1.** Black + ruff + mypy + pytest on staged files. You'll never push broken code.
3. **One README + one CHANGELOG, updated as you go.** Don't write them the night before the presentation.
4. **Use `uv` or `poetry` for dependency management** — not `pip install` ad-hoc. Reproducibility is graded.
5. **Seeds everywhere.** `torch.manual_seed(42); np.random.seed(42); random.seed(42)`. Deterministic ML demos = professional ML demos.
6. **Office hours.** Email the prof before Aula 6 with concrete questions on your project. Cheapest senior-eng feedback available.
7. **Teach a teammate.** Explaining `autograd` to someone is the best way to learn `autograd`.

---

## Open questions to confirm with the professor (Aula 1)

1. Are deliverables 3 and 4 really swapped in date order, or is that a typo in the calendar?
2. Classroom code (cell B10 in spreadsheet was empty) — what is it?
3. Apresentação: rubric weights — how much is engenharia (tests/git/arch) vs ML quality?
4. Is there a preferred dataset / problem domain or open choice for the project?
