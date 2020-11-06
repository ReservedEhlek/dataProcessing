CREATE TABLE public.conditions
(
    "time" timestamp with time zone,
    light numeric,
    temp integer,
    humidity numeric,
    visibility integer,
    PRIMARY KEY ("time"),
    CONSTRAINT "time" FOREIGN KEY ("time")
        REFERENCES public.geolocation ("time") MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
);

ALTER TABLE public.conditions
    OWNER to postgres;