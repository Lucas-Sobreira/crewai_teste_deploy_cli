CREATE TABLE IF NOT EXISTS public.bitcoin(
  id                    BIGSERIAL PRIMARY KEY,
  ativo                 TEXT NOT NULL,
  preco                 NUMERIC (18,6)
  moeda                 CHAR(3) NOT NULL DEFAULT 'USD',
  horario_coleta        TIMESTAMPTZ NOT NULL,
  inserido_em           TIMESTAMPTZ NOT NULL DEFAULT NOW()
)