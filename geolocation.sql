CREATE TABLE public.geolocation
(
    "X" numeric NOT NULL,
    "Y" numeric NOT NULL,
    "time" timestamp with time zone,
    PRIMARY KEY ("time")
);

ALTER TABLE public.geolocation
    OWNER to postgres;