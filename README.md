# Novel Language in Context

### An Exploratory NLP Study

## Overview

This project explores how novel lexical formations are represented and interpreted in context, combining linguistic analysis with computational NLP methods.

The investigation originated from naturally occurring creative language in human–AI conversations, particularly the use of *Frankenstein* as a productive linguistic expression beyond its conventional meaning.

Using a small, manually curated conversational corpus, the project examines how different NLP approaches represent unfamiliar expressions and how conversational context contributes to their interpretation.

The study is organised into two stages.

## Research Plan

### Experiment A — Lexical Representation

**Status: In progress**

Investigate how different NLP approaches represent novel lexical formations and their contextual uses.

The planned investigation includes:

- Lexical exploration and corpus analysis.
- Traditional text representations, including Bag-of-Words and TF-IDF.
- Static word embeddings.
- Contextual embeddings.

The specific comparisons and evaluation procedures will be developed as the investigation progresses.

### Experiment B — Contextual Interpretation and Conversational Continuation

**Status: Future work**

Explore how language models respond to novel expressions within conversational contexts, including the continuation and extension of figurative language.

This stage may involve controlled comparisons to investigate how particular linguistic cues influence model responses.

Its experimental design will be developed after Experiment A.

## Data

The initial corpus consists of 10 manually selected human–AI conversational exchanges containing creative uses of *Frankenstein* and related expressions.

Each exchange contains a user prompt and an assistant response.

The original conversations have been extracted, structured, preprocessed and validated. Raw and processed conversational data are excluded from version control.

A reader-friendly version of the ten selected conversational exchanges is available in the [Adapted Exchange Guide](docs/corpus/adapted_exchanges.md). The guide includes contextual information and linguistic observations illustrating how creative expressions are introduced, reused and extended throughout the conversations.

The excerpts have been edited for readability and discretion. They are intended to make the linguistic phenomena accessible to readers and are not used as the analytical corpus. Computational analyses use the separately preserved conversational data.

## Current Progress

**Completed**
- PDF text extraction and conversational exchange identification.
- Structured JSON corpus creation.
- Text preprocessing and formatting normalisation.
- Structural validation and selected Unicode preservation checks.
- Initial Git version-control setup.

**Next**
- Lexical exploration of the cleaned corpus.
- Development of Experiment A.

## Project Status

This is an exploratory project under active development. Research questions, methods and documentation may be refined as the analysis progresses.
