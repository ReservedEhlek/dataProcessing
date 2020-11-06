CREATE TABLE public."eyeTracking"
(
    "time" timestamp with time zone NOT NULL,
    "eye1X" integer NOT NULL,
    "eye1Y" integer NOT NULL,
    "eye2X" integer NOT NULL,
    "eye2Y" integer NOT NULL,
    "soc1X" integer NOT NULL,
    "soc1Y" integer NOT NULL,
    "soc2X" integer NOT NULL,
    "soc2Y" integer NOT NULL,
    PRIMARY KEY ("time")
);

ALTER TABLE public."eyeTracking"
    OWNER to postgres;