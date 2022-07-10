MODULE_NAME=LinuxEp
MODULE_OBJ=$(MODULE_NAME).o
MODULE_OUT=$(MODULE_NAME).ko

obj-m+=$(MODULE_OBJ)

KERNEL_PATH?=/lib/modules/$(shell uname -r)/build/

MODULE_OUT:
	@echo "KERNEL_PATH: $(KERNEL_PATH)"
	@echo "TARGET_ABI: $(TARGET_ABI)"

	ln -nfs $(MODULE_OBJ).$(TARGET_ABI) $(MODULE_OBJ)
	ln -nfs LoLeLinuxDrv.o.$(TARGET_ABI) LoLeLinuxDrv.o
	ln -nfs LoLeLinuxMem.o.$(TARGET_ABI) LoLeLinuxMem.o

	touch .LinuxEp.o.cmd
	touch .LoLeLinuxMem.o.cmd
	touch .LoLeLinuxDrv.o.cmd

	make -C $(KERNEL_PATH) M=$(PWD) modules

clean:
	make -C $(KERNEL_PATH) M=$(PWD) clean
	rm -f $(MODULE_OBJ) LoLeLinuxDrv.o LoLeLinuxMem.o
	rm -f .LinuxEp.o.cmd
	rm -f .LoLeLinuxMem.o.cmd
	rm -f .LoLeLinuxDrv.o.cmd

$(MODULE_NAME)-objs := LoLeLinuxDrv.o LoLeLinuxMem.o
